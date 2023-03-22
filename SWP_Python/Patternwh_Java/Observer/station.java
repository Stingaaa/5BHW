import java.util.ArrayList;
import java.util.List;

abstract class stations {
    protected List<display> displays = new ArrayList<display>(); 

    public void addDisplay(display d) { 
        displays.add(d); 
    } 

    public void removeDisplay(display d) { 
        displays.remove(d); 
    } 

    //Push
    protected void sendData(Weather w) { 
        for (display d : displays) { 
            d.getWeather(w); 
        } 
    } 

    //Pull
    protected void notifySubs(){
        for (display d : displays){
            break;
        }
    }
}

class station extends stations{
    private Weather weather; 

    @Override
    protected void notifySubs(){
        for (display d : displays){
            d.sendNotification(this);
        }
    }

    //Push
    public void setWeather(Weather w) { 
        this.weather = w; 
        sendData(w); 
    } 

    //Pull
    public void setWeatherPull(Weather w){
        this.weather = w;
        notifySubs();
    }

    //Push
    public Weather getWeather() { 
        return this.weather; 
    } 

    //Pull
    public Weather requestWeather(){
        return this.weather;
    }
}