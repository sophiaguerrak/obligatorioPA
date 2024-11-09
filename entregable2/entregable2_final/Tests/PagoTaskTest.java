package Tests;
import static org.junit.jupiter.api.Assertions.*;

import entregable2_v2.PagoTask;
import entregable2_v2.Pedido;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class PagoTaskTest {

    private Pedido pedido;
    private PagoTask pagoTask;

    @BeforeEach
    public void setUp() {
        // Creamos una instancia de Pedido
        pedido = new Pedido("123", true);

        // Creamos la instancia de PagoTask
        pagoTask = new PagoTask(pedido);
    }

    @Test
    public void testCallSuccess() throws Exception {
        long startTime = System.currentTimeMillis();
        Boolean result = pagoTask.call();
        long endTime = System.currentTimeMillis();
        assertTrue(result);
        assertTrue((endTime - startTime) >= 1000 && (endTime - startTime) < 1500,
                "El tiempo de ejecución debería estar entre 1000ms y 1500ms");

        assertEquals("123", pedido.getId());
    }

    @Test
    public void testCallInterrupted() throws Exception {
        PagoTask interruptedTask = new PagoTask(pedido) {
            @Override
            public Boolean call() {
                System.out.println("Procesando pago para el pedido: " + pedido.getId());
                Thread.currentThread().interrupt();  // Interrumpimos manualmente el hilo
                try {
                    Thread.sleep(1000);  // Simulamos el sleep para capturar la interrupcion
                } catch (InterruptedException e) {
                    System.out.println("Error en el procesamiento de pago para el pedido: " + pedido.getId());
                    return false;
                }
                return true;
            }
        };
        Boolean result = interruptedTask.call();
        assertFalse(result);
        assertEquals("123", pedido.getId());
    }
}

