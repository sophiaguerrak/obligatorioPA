package Tests;
import static org.junit.jupiter.api.Assertions.*;
import entregable2_v2.Pedido;
import org.junit.jupiter.api.Test;

public class PedidoTest {

    @Test
    public void testGetId() {
        Pedido pedido = new Pedido("123", false);
        assertEquals("123", pedido.getId());
    }

    @Test
    public void testEsUrgenteTrue() {
        Pedido pedido = new Pedido("123", true);
        assertTrue(pedido.esUrgente());
    }

    @Test
    public void testEsUrgenteFalse() {
        Pedido pedido = new Pedido("123", false);
        assertFalse(pedido.esUrgente());
    }

    @Test
    public void testCompareTo_UrgenteVsNoUrgente() {
        Pedido pedidoUrgente = new Pedido("001", true);
        Pedido pedidoNoUrgente = new Pedido("002", false);

        assertTrue(pedidoUrgente.compareTo(pedidoNoUrgente) < 0);
    }

    @Test
    public void testCompareTo_NoUrgenteVsUrgente() {
        Pedido pedidoUrgente = new Pedido("001", true);
        Pedido pedidoNoUrgente = new Pedido("002", false);
        assertTrue(pedidoNoUrgente.compareTo(pedidoUrgente) > 0);
    }

    @Test
    public void testCompareTo_MismoTipoPedido() {
        Pedido pedidoUrgente1 = new Pedido("001", true);
        Pedido pedidoUrgente2 = new Pedido("002", true);
        Pedido pedidoNoUrgente1 = new Pedido("003", false);
        Pedido pedidoNoUrgente2 = new Pedido("004", false);
        assertEquals(0, pedidoUrgente1.compareTo(pedidoUrgente2));
        assertEquals(0, pedidoNoUrgente1.compareTo(pedidoNoUrgente2));
    }
}
