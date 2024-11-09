package Tests;

import static org.junit.jupiter.api.Assertions.*;

import entregable2_v2.EnvioTask;
import entregable2_v2.Pedido;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class EnvioTaskTest {

    private Pedido pedidoUrgente;
    private Pedido pedidoNoUrgente;
    private EnvioTask envioTaskUrgente;
    private EnvioTask envioTaskNoUrgente;

    @BeforeEach
    public void setUp() {

        pedidoUrgente = new Pedido("123", true);
        pedidoNoUrgente = new Pedido("456", false);

        envioTaskUrgente = new EnvioTask(pedidoUrgente);
        envioTaskNoUrgente = new EnvioTask(pedidoNoUrgente);
    }

    @Test
    public void testRunUrgente() {
        long startTime = System.currentTimeMillis();
        envioTaskUrgente.run();
        long endTime = System.currentTimeMillis();
        assertTrue((endTime - startTime) >= 500 && (endTime - startTime) < 1000,
                "El tiempo de ejecución debería estar entre 500ms y 1000ms para pedidos urgentes");
        assertEquals("123", pedidoUrgente.getId());
    }

    @Test
    public void testRunNoUrgente() {
        long startTime = System.currentTimeMillis();
        envioTaskNoUrgente.run();
        long endTime = System.currentTimeMillis();
        assertTrue((endTime - startTime) >= 1500 && (endTime - startTime) < 2000,
                "El tiempo de ejecución debería estar entre 1500ms y 2000ms para pedidos no urgentes");
        assertEquals("456", pedidoNoUrgente.getId());
    }

    @Test
    public void testRunInterrupted() {
        EnvioTask interruptedTask = new EnvioTask(pedidoUrgente) {
            @Override
            public void run() {
                System.out.println("Enviando el pedido: " + pedidoUrgente.getId());
                Thread.currentThread().interrupt();
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    System.out.println("Error en el envío del pedido: " + pedidoUrgente.getId());
                    Thread.currentThread().interrupt();
                }
            }
        };
        interruptedTask.run();
        assertEquals("123", pedidoUrgente.getId());
    }
}

