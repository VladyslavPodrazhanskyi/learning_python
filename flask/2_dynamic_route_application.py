from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>This is HOME page!</h1>"



@app.route('/<name>')    #!!! адрес прописывается в теге ( все после / попадает в функцию как аргумент
def name(name): # name - обязательный аргумент для функции представления.
    return "<h1>Hello, %s!</h1>" % name     # %s -  заполниител в html

if __name__ == "__main__":
    app.run(debug=True)
