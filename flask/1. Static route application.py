from flask import Flask

app = Flask(__name__)    # создание экземпляра приложения flask

@app.route("/")    # декоратор (привязка функции к url адресу) позволяет задать путь в котором будет размещаться шаблон
def index():            # view function формирует ответ на запрос
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run(debug=True)      # fuser -n tcp -k 5000  - очистка сервера.



