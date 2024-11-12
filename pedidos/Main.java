public class Main {
    public static void main(String[] args) {
        ProcesadorPedidos procesador = new ProcesadorPedidos(50);

        // simulamos pedidos concurrentes
        for (int i = 1; i <= 100; i++) {
            boolean esUrgente = (i % 5 == 0);  //cada 5 pedidos, 1 es urgente
            Pedido pedido = new Pedido("Pedido-" + i, esUrgente);
            procesador.agregarPedido(pedido);  
        }
        procesador.procesarPedidos();
        procesador.shutdown();
        procesador.imprimirResultados();
    }
}