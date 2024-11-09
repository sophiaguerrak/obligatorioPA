package Tests;

import static org.junit.jupiter.api.Assertions.*;

import entregable2_v2.EmpaquetadoTask;
import entregable2_v2.Pedido;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class EmpaquetadoTaskTest {

    private Pedido pedido;
    private EmpaquetadoTask empaquetadoTask;

    @BeforeEach
    public void setUp() {
        // Creamos una instancia de Pedido
        pedido = new Pedido("123", true);

        // Creamos la instancia de EmpaquetadoTask con el Pedido
        empaquetadoTask = new EmpaquetadoTask(pedido);
    }

    @Test
    public void testCallSuccess() throws Exception {
        // Medimos el tiempo inicial antes de ejecutar call
        long startTime = System.currentTimeMillis();

        // Ejecutamos el método call
        Boolean result = empaquetadoTask.call();

        // Medimos el tiempo final despues de ejecutar call
        long endTime = System.currentTimeMillis();

        // Verificamos que el metodo devuelve true
        assertTrue(result);

        // Verificamos que el metodo sleep fue invocado (minimo 2 segundos)
        assertTrue((endTime - startTime) >= 2000);

        // Verificamos que el ID del pedido es el esperado
        assertEquals("123", pedido.getId());
    }

    @Test
    public void testCallInterrupted() throws Exception {
        // Creamos una subclase de EmpaquetadoTask para simular una interrupcion
        EmpaquetadoTask interruptedTask = new EmpaquetadoTask(pedido) {
            @Override
            public Boolean call() {
                System.out.println("Empaquetando el pedido: " + pedido.getId());
                Thread.currentThread().interrupt();  // Interrumpimos manualmente el hilo
                try {
                    Thread.sleep(2000);  // Simulamos el sleep para capturar la interrupción
                } catch (InterruptedException e) {
                    System.out.println("Error en el empaquetado del pedido: " + pedido.getId());
                    return false;
                }
                return true;
            }
        };

        // Ejecutamos el metodo call que deberia interrumpirse
        Boolean result = interruptedTask.call();

        // Verificamos que el metodo devuelve false tras la interrupcion
        assertFalse(result);

        // Verificamos que el ID del pedido es el que esperado
        assertEquals("123", pedido.getId());
    }
}

