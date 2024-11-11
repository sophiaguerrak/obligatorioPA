package entregable2_v2;

import java.util.concurrent.Callable;

public class EmpaquetadoTask implements Callable<Boolean> {
    private final Pedido pedido;

    public EmpaquetadoTask(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public Boolean call() {
        System.out.println("Empaquetando el pedido: " + pedido.getId());
        try {
            Thread.sleep(2000); 
            System.out.println("Empaque listo para el pedido: " + pedido.getId());
            return true;  
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("Error en el empaquetado del pedido: " + pedido.getId());
            return false;  
        }
    }
}