public class test{
    public static void main(String[] args) {
        station s = new station();
        display d1 = new display("Display 1");
        display d2 = new display("Display 2");
        s.addDisplay(d1);
        s.addDisplay(d2);
        Weather sunny = new Weather("Sunny - 21 Degrees");
        Weather rainy = new Weather("Rain - 14 Degrees");
        s.setWeather(sunny);
        s.removeDisplay(d1);
        s.setWeather(rainy);

        System.out.println("______________________________");
        
        s.setWeatherPull(sunny);
        s.addDisplay(d1);
        s.setWeather(rainy);
    }
}