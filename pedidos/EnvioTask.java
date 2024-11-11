package entregable2_v2;

public class EnvioTask implements Runnable {
    private final Pedido pedido;

    public EnvioTask(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public void run() {
        System.out.println("Enviando el pedido: " + pedido.getId());
        try {
            Thread.sleep(pedido.esUrgente() ? 500 : 1500);  // demora menos si es urgente (envio rápido)
            System.out.println("Pedido enviado: " + pedido.getId());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("Error en el envío del pedido: " + pedido.getId());
        }
    }
}