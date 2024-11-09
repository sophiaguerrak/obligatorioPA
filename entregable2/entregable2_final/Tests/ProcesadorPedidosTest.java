package Tests;
import static org.junit.jupiter.api.Assertions.*;
import entregable2_v2.PagoTask;
import entregable2_v2.Pedido;
import entregable2_v2.ProcesadorPedidos;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class ProcesadorPedidosTest {

    private ProcesadorPedidos procesadorPedidos;

    @BeforeEach
    public void setUp() {
        // Inicializamos el ProcesadorPedidos con 2 hilos
        procesadorPedidos = new ProcesadorPedidos(2);
    }

    @Test
    public void testAgregarPedidoYProcesarExitoso() throws Exception {
        // Creamos dos pedidos, uno urgente y otro comun
        Pedido pedidoNormal = new Pedido("001", false);
        Pedido pedidoUrgente = new Pedido("002", true);

        // Agregamos los pedidos a la cola
        procesadorPedidos.agregarPedido(pedidoNormal);
        procesadorPedidos.agregarPedido(pedidoUrgente);

        // Procesamos los pedidos
        procesadorPedidos.procesarPedidos();

        // Esperamos un tiempo para permitir que los hilos completen las tareas
        procesadorPedidos.shutdown();

        // Validamos que los resultados del procesamiento son los esperados
        procesadorPedidos.imprimirResultados();

        // Las verificaciones adicionales podrían incluir chequear que el tiempo total no es cero
        assertTrue(procesadorPedidos.tiempoTotalNormal > 0);
        assertTrue(procesadorPedidos.tiempoTotalUrgente > 0);
    }


    @Test
    public void testShutdown() {
        // Agregamos un pedido normal
        Pedido pedidoNormal = new Pedido("004", false);
        procesadorPedidos.agregarPedido(pedidoNormal);

        // Procesamos el pedido
        procesadorPedidos.procesarPedidos();

        // Intentamos hacer un shutdown limpio
        procesadorPedidos.shutdown();

        // Verificamos que el shutdown haya sido correcto
        assertTrue(procesadorPedidos.executorService.isShutdown());
    }

    @Test
    public void testProcesarSinPedidos() {
        // Procesamos sin haber agregado pedidos
        procesadorPedidos.procesarPedidos();

        // No debe haber errores, y el tiempo de procesamiento debe ser 0
        procesadorPedidos.imprimirResultados();

        // Verificamos que no se proceso ningun pedido
        assertEquals(0, procesadorPedidos.tiempoTotalNormal);
        assertEquals(0, procesadorPedidos.tiempoTotalUrgente);
        assertEquals(0, procesadorPedidos.contadorNormal);
        assertEquals(0, procesadorPedidos.contadorUrgente);
    }
}
