from flask import Flask


app = Flask(__name__)

help(Flask)

@app.route('/')
def index():
    return "<h1>This is HOME page!</h1>"



@app.route('/<name>')    #!!! адрес прописывается в теге. 
def name(name):
    return "<h1>Hello, %s!</h1>" % name     # %s -  заполниител в html (можно заменить {{name}} jinja2

if __name__ == "__main__":
    app.run(debug=True)
