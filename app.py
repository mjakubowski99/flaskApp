from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(a+b)