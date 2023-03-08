import cgi
import json
import time
from flask import Flask, render_template, request
from flask_restful import Api
import webbrowser
import paho.mqtt.client as paho
from paho import mqtt
import pdb
import pandas as p
import plotly
import plotly.express as px
from tkinter import filedialog as fd

app = Flask(__name__)
api = Api(app)

def getStatistic():
    with open("SWP-Python\SteinScherePapierEchseSpock/flask_saves.txt", "r") as s:
        return json.load(s)

@app.route('/',methods=["GET", "POST"])
def start():
    if request.method == "POST":
        stats = getStatistic()
        user = request.form.get("username")
        userPos = stats[0].index(user)
        userStats = stats[userPos+1]
        keys = list(userStats.keys())
        
        outs = []
        for i in range(0,3):
            outs.append([keys[i], userStats[keys[i]], i])
        dO = p.DataFrame(outs, columns=["type", "count", "col"])
        
        items = []
        for j in range(3,8):
            items.append([keys[j], userStats[keys[j]], j])
        dI = p.DataFrame(items, columns=["type", "count", "col"])
        
        figO = px.bar(dO, x="type", y="count", color="col")
        graphO = json.dumps(figO, cls=plotly.utils.PlotlyJSONEncoder)
        
        figI = px.bar(dI, x="type", y="count", color="col")
        graphI = json.dumps(figI, cls=plotly.utils.PlotlyJSONEncoder)
            
        return render_template("stats.html", outs=graphO, items=graphI)
    
    if request.method == "GET":
        return render_template("main.html")
    
@app.route('/upload', methods=["GET","POST"])
def upload():
    if request.method == "POST":
        file = json.load(fd.askopenfile())
        with open("SWP-Python\SteinScherePapierEchseSpock/flask_saves.txt", "w") as flask:
            flask.write(json.dumps(file))
    return render_template("main.html")

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run()