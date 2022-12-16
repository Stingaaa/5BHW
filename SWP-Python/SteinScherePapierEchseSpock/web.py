from flask import Flask, render_template, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/',methods=["GET", "POST"])
def start():
    if request.method == "POST":
        user = request.form.get("username")
        print(user)
        s = user
        return render_template("stats.html", stats = s)
    return render_template("main.html")

if __name__ == '__main__':
    app.run()