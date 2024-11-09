package entregable2_v2;

public class Pedido implements Comparable<Pedido> {
    private final String id;
    private final boolean esUrgente;

    public Pedido(String id, boolean esUrgente) {
        this.id = id;
        this.esUrgente = esUrgente;
    }

    public String getId() {
        return id;
    }

    public boolean esUrgente() {
        return esUrgente;
    }

    @Override
    public int compareTo(Pedido otroPedido) {
        // para priorizar los urgentes
        return Boolean.compare(otroPedido.esUrgente, this.esUrgente);
    }
}