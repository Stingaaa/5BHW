package SWP_Python.Patternwh_Java.Factory;

public class Pizzaplaces {
    public static void main(String[] args) {
        Pizzeria h = new HamburgPizzeria();
        Pizzeria b = new BerlinPizzeria();
        Pizzeria r = new RostockPizzeria();

        b.erstellePizza(Pizza.Prosciutto);
        h.erstellePizza(Pizza.Calzone);
        r.erstelleSpezial();
        b.erstelleSpezial();
        h.erstelleSpezial();
    }
}