package entregable2_v2;

import java.util.concurrent.Callable;

public class PagoTask implements Callable<Boolean> {
    private final Pedido pedido;

    public PagoTask(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public Boolean call() {
        System.out.println("Procesando pago para el pedido: " + pedido.getId());
        try {
            Thread.sleep(1000);  
            System.out.println("Pago autorizado para el pedido: " + pedido.getId());
            return true;  
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("Error en el procesamiento de pago para el pedido: " + pedido.getId());
            return false; 
        }
    }
}