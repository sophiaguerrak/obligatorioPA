public class TestsUnificados {

    public static void main(String[] args) {
        EmpaquetadoTaskTest();
        EnvioTaskTest();
        PagoTaskTest();
        PedidoTest();
        ProcesadorPedidosTest();
    }

    private static void assertTrue(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError("Test failed: " + message);
        }
    }

    private static void assertFalse(boolean condition, String message) {
        if (condition) {
            throw new AssertionError("Test failed: " + message);
        }
    }

    private static void assertEquals(Object expected, Object actual, String message) {
        if (!expected.equals(actual)) {
            throw new AssertionError("Test failed: " + message + " Expected: " + expected + ", but got: " + actual);
        }
    }

    // EmpaquetadoTask Tests
    public static void EmpaquetadoTaskTest() {
        Pedido pedido = new Pedido("123", true);
        EmpaquetadoTask empaquetadoTask = new EmpaquetadoTask(pedido);

        try {
            long startTime = System.currentTimeMillis();
            Boolean result = empaquetadoTask.call();
            long endTime = System.currentTimeMillis();

            assertTrue(result, "EmpaquetadoTaskTest: El resultado debería ser true");
            assertTrue((endTime - startTime) >= 2000, "EmpaquetadoTaskTest: El tiempo de ejecución debería ser al menos 2000ms");
            assertEquals("123", pedido.getId(), "EmpaquetadoTaskTest: El ID debería ser 123");

            EmpaquetadoTask interruptedTask = new EmpaquetadoTask(pedido) {
                @Override
                public Boolean call() {
                    Thread.currentThread().interrupt();
                    try {
                        Thread.sleep(2000);
                    } catch (InterruptedException e) {
                        return false;
                    }
                    return true;
                }
            };

            assertFalse(interruptedTask.call(), "EmpaquetadoTaskTest: El resultado debería ser false tras la interrupción");
        } catch (Exception e) {
            System.out.println("EmpaquetadoTaskTest falló: " + e.getMessage());
        }
    }

    // EnvioTask Tests
    public static void EnvioTaskTest() {
        Pedido pedidoUrgente = new Pedido("123", true);
        EnvioTask envioTaskUrgente = new EnvioTask(pedidoUrgente);

        long startTime = System.currentTimeMillis();
        envioTaskUrgente.run();
        long endTime = System.currentTimeMillis();
        assertTrue((endTime - startTime) >= 500 && (endTime - startTime) < 1000, 
                   "EnvioTaskTest: Tiempo de ejecución entre 500ms y 1000ms para pedidos urgentes");
        assertEquals("123", pedidoUrgente.getId(), "EnvioTaskTest: ID debería ser 123");

        Pedido pedidoNoUrgente = new Pedido("456", false);
        EnvioTask envioTaskNoUrgente = new EnvioTask(pedidoNoUrgente);

        startTime = System.currentTimeMillis();
        envioTaskNoUrgente.run();
        endTime = System.currentTimeMillis();
        assertTrue((endTime - startTime) >= 1500 && (endTime - startTime) < 2000, 
                   "EnvioTaskTest: Tiempo de ejecución entre 1500ms y 2000ms para pedidos no urgentes");

        EnvioTask interruptedTask = new EnvioTask(pedidoUrgente) {
            @Override
            public void run() {
                Thread.currentThread().interrupt();
                try {
                    Thread.sleep(500);
                } catch (InterruptedException ignored) {}
            }
        };

        interruptedTask.run();
        assertEquals("123", pedidoUrgente.getId(), "EnvioTaskTest: ID debería ser 123 tras la interrupción");
    }

    // PagoTask Tests
    public static void PagoTaskTest() {
        Pedido pedido = new Pedido("123", true);
        PagoTask pagoTask = new PagoTask(pedido);

        try {
            long startTime = System.currentTimeMillis();
            Boolean result = pagoTask.call();
            long endTime = System.currentTimeMillis();

            assertTrue(result, "PagoTaskTest: Resultado debería ser true");
            assertTrue((endTime - startTime) >= 1000 && (endTime - startTime) < 1500, 
                       "PagoTaskTest: Tiempo de ejecución entre 1000ms y 1500ms");
            assertEquals("123", pedido.getId(), "PagoTaskTest: ID debería ser 123");

            PagoTask interruptedTask = new PagoTask(pedido) {
                @Override
                public Boolean call() {
                    Thread.currentThread().interrupt();
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        return false;
                    }
                    return true;
                }
            };

            assertFalse(interruptedTask.call(), "PagoTaskTest: Resultado debería ser false tras la interrupción");
        } catch (Exception e) {
            System.out.println("PagoTaskTest falló: " + e.getMessage());
        }
    }

    // Pedido Tests
    public static void PedidoTest() {
        Pedido pedido = new Pedido("123", false);
        assertEquals("123", pedido.getId(), "PedidoTest: ID debería ser 123");
        assertTrue(new Pedido("123", true).esUrgente(), "PedidoTest: esUrgente debería ser true");

        Pedido pedidoUrgente = new Pedido("001", true);
        Pedido pedidoNoUrgente = new Pedido("002", false);

        assertTrue(pedidoUrgente.compareTo(pedidoNoUrgente) < 0, "PedidoTest: Urgente debe ser menor que no urgente");
        assertTrue(pedidoNoUrgente.compareTo(pedidoUrgente) > 0, "PedidoTest: No urgente debe ser mayor que urgente");
    }

    // ProcesadorPedidos Tests
    public static void ProcesadorPedidosTest() {
        ProcesadorPedidos procesadorPedidos = new ProcesadorPedidos(2);
        Pedido pedidoNormal = new Pedido("001", false);
        Pedido pedidoUrgente = new Pedido("002", true);

        procesadorPedidos.agregarPedido(pedidoNormal);
        procesadorPedidos.agregarPedido(pedidoUrgente);
        procesadorPedidos.procesarPedidos();
        procesadorPedidos.shutdown();

        assertTrue(procesadorPedidos.tiempoTotalNormal > 0, "ProcesadorPedidosTest: tiempoTotalNormal > 0");
        assertTrue(procesadorPedidos.tiempoTotalUrgente > 0, "ProcesadorPedidosTest: tiempoTotalUrgente > 0");

        procesadorPedidos = new ProcesadorPedidos(2);
        procesadorPedidos.shutdown();
        assertTrue(procesadorPedidos.executorService.isShutdown(), "ProcesadorPedidosTest: Executor debería estar apagado");
    }
}