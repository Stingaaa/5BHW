import cgi
import time
from flask import Flask, render_template, request
from flask_restful import Api
import webbrowser
import paho.mqtt.client as paho
from paho import mqtt
import pdb

app = Flask(__name__)
api = Api(app)

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    m = str(msg.payload.decode("utf-8")).split("-")
    c, n = generateClient()
    print(m)
    if(n != m[0]):
        if(m[1] == "user"):
            match m[2]:
                case "known":
                        app.name = "home-" + app.name
                case "unknown":
                        app.name = "agb-" + app.name
        if(m[1] == "play"):
            old = app.name.split("-")
            if len(old) == 3:
                app.name = old[0] + "-" + old[1] + "-" + m[2]
            else:
                app.name = app.name+"-"+m[2]

def generateClient():
    name = "web"
    client = paho.Client(client_id=name, userdata=None, protocol=paho.MQTTv5)
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set("Stingaaa", "test1234")
    client.connect("15d9dcdf33e3466799ebbd0151f866ee.s2.eu.hivemq.cloud", 8883)
    client.on_message = on_message
    client.subscribe("game", qos=1)
    return client, name

@app.route('/',methods=["GET", "POST"])
def start():
    if request.method == "POST":
        user = request.form.get("username")
        app.name=user
        c, n = generateClient()
        c.loop_start()
        c.publish("game", n+"-user-"+user, 1)
        for i in range(10):    
            time.sleep(0.1)
            print()
        c.loop_stop()
        return render_template(app.name.split("-")[0]+".html", user=app.name.split("-")[1], imgP="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpIjHcsid48ItMU-3AGR9a6oKjTw8zyWVfQ&usqp=CAU", imgPC="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpIjHcsid48ItMU-3AGR9a6oKjTw8zyWVfQ&usqp=CAU")
    
    if request.method == "GET":
        return render_template("main.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    c, n = generateClient()
    item = request.form.get("item")
    nr = 1 if item == "stone" else 2 if item == "scissor" else 3 if item == "paper" else 4 if item == "lizard" else 5 if item == "spock" else 6
    c.loop_start()
    c.publish("game", n+"-play-"+app.name.split("-")[1]+"-"+str(nr), 1)
    for i in range(10):    
        time.sleep(0.1)
        print()
        c.loop_stop()
    return render_template(app.name.split("-")[0]+".html", user=app.name.split("-")[1], imgP=request.form.get(app.name.split("-")[2]), imgPC=request.form.get(app.name.split("-")[3]), out=app.name.split("-")[4].split("m")[1])

@app.route('/agb',methods=["GET", "POST"])
def agb():
    return render_template("home.html", user=app.name.split("-")[1], imgP="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpIjHcsid48ItMU-3AGR9a6oKjTw8zyWVfQ&usqp=CAU", imgPC="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpIjHcsid48ItMU-3AGR9a6oKjTw8zyWVfQ&usqp=CAU")

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run()