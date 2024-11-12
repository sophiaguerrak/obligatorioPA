import java.util.concurrent.*;
import java.util.PriorityQueue;

public class ProcesadorPedidos {
    public final ExecutorService executorService;
    private final PriorityQueue<Pedido> colaPedidos;
    public long tiempoTotalNormal;
    public long tiempoTotalUrgente;
    public int contadorNormal;
    public int contadorUrgente;

    public ProcesadorPedidos(int numHilos) {
        this.executorService = Executors.newFixedThreadPool(numHilos);
        this.colaPedidos = new PriorityQueue<>();
        this.tiempoTotalNormal = 0;
        this.tiempoTotalUrgente = 0;
        this.contadorNormal = 0;
        this.contadorUrgente = 0;
    }

    public void agregarPedido(Pedido pedido) {
        colaPedidos.add(pedido); 
    }

    public void procesarPedidos() {
        while (!colaPedidos.isEmpty()) {
            Pedido pedido = colaPedidos.poll(); 
            if (pedido != null) {
                executorService.submit(() -> {
                    long inicioPedido = System.currentTimeMillis(); 
                    boolean pagoExitoso = new PagoTask(pedido).call();
                    if (pagoExitoso) {
                        boolean empaquetadoExitoso = new EmpaquetadoTask(pedido).call();
                        if (empaquetadoExitoso) {
                            new EnvioTask(pedido).run();
                        } else {
                            System.out.println("El pedido no se pudo empaquetar: " + pedido.getId());
                        }
                    } else {
                        System.out.println("El pago falló para el pedido: " + pedido.getId());
                    }
                    long finPedido = System.currentTimeMillis(); 
                    long tiempoTotal = finPedido - inicioPedido; 

                    if (pedido.esUrgente()) {
                        tiempoTotalUrgente += tiempoTotal;
                        contadorUrgente++;
                    } else {
                        tiempoTotalNormal += tiempoTotal;
                        contadorNormal++;
                    }
                });
            }
        }
    }

    public void imprimirResultados() {
        double promedioNormal = contadorNormal > 0 ? (double) tiempoTotalNormal / contadorNormal : 0;
        double promedioUrgente = contadorUrgente > 0 ? (double) tiempoTotalUrgente / contadorUrgente : 0;

        System.out.printf("\nPromedio de tiempos de procesamiento para pedidos normales: %.2f ms%n", promedioNormal);
        System.out.printf("Promedio de tiempos de procesamiento para pedidos urgentes: %.2f ms%n", promedioUrgente);
    }

    public void shutdown() {
        executorService.shutdown();
        try {
            if (!executorService.awaitTermination(60, TimeUnit.SECONDS)) {
                executorService.shutdownNow();
            }
        } catch (InterruptedException e) {
            executorService.shutdownNow();
        }
    }
}