from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    print(request.cookies, request.headers)
    return "Hello World!"
