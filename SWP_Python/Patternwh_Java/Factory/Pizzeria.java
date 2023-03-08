package SWP_Python.Patternwh_Java.Factory;

public abstract class Pizzeria{
    public void erstellePizza(Pizza p){
        System.out.println(p + " wird gebacken und verpackt, usw.");
    }

    public abstract void erstelleSpezial();
}