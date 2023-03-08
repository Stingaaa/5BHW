package SWP_Python.Patternwh_Java.Factory;

class HamburgPizzeria extends Pizzeria{

    @Override
    public void erstelleSpezial() {
        System.out.println("Gibts ned");
    }

}

class RostockPizzeria extends Pizzeria{

    @Override
    public void erstelleSpezial() {
        System.out.println("Rostock Spezial wird zubereitet usw.");
    }

}

class BerlinPizzeria extends Pizzeria{

    @Override
    public void erstelleSpezial() {
        System.out.println("Berlin Spezial wird zubereitet usw.");
    }

}