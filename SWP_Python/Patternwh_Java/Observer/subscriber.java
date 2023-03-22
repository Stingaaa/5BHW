interface displays {
    public void getWeather(Weather w);
}

class display implements displays{

    private String displayName;

    public display(String name){
        this.displayName = name;
    }

    //Push
    public void getWeather(Weather w) {
        System.out.println(this.displayName + ": " + w.getWeatherData());
    }

    //Pull
    public void sendNotification(station s){
        System.out.println(this.displayName + ":" + s.requestWeather().getWeatherData());
    }
}