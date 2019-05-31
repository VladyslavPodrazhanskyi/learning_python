from flask import Flask, render_template

app = Flask(__name__)


# 1.Routing and variables

@app.route("/")
def home():
    return "<h1>It's my base page</h1>"

@app.route("/str/<string>")
def get_str(string):
    if isinstance(string, str):
        return f"<h1>Your string is {string}</h1>"

@app.route("/int/<int:number>")
def get_int(number):
    if isinstance(number, int):
        return f"<h1>Your int number is {number}</h1>"


@app.route("/float/<float:number>")       # ввод переменной  <converter:variable_name>
def get_float(number):
    if isinstance(number, float):
        return f"<h1>Your float number is {number}</h1>"


@app.route("/path/<path:path>")
def get_path(path):
    return f"<h1>You entered following path: {path}.</h1>"


@app.route("/name/<int:index>")
def get_name(index):
    names = ["Rita", "Elena", "Sergey"]
    try:
        return f"<h1>Name for this index is {names[index]}</h1>"
    except IndexError:
        return "<h1>Your index is out of range!</h1>"


@app.route("/file/<path:val>")
def from_file(val):
    with open(val) as file:
        return f"<h1>{file.read()}</h1>"

@app.route("/uuid/<uuid:val>")
def get_uuid(val):
    return f"<h1>My UUID is: {val}</h1>"


# 2. Rendering templates

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/name")
@app.route("/name/<name>")
def get_hello(name=None):
    if name:
        return render_template("hello.html", name=name)
    else:
        return render_template("hello.html")



#3. http methods.

# @app.route("/login", methods=["GET", "POST"]) # декоратор содержит аргумент methods- GET by default
# def login():
#     if request.method == "POST":
#         return do_the_login()
#     else:
#         return show_the_login_form()


test_methods =  ["Value1", "Value2"]   # имитируем базу данных


def do_post(value):
    """
    This method will add value to the test_methods_dict
    :return:
    """
    return test_methods_.append(value)
# #
# #
# # def do_get():
# #     """
# #     Returns template with all test_methods_dict values
# #     :return:
# #     """
# #     return render_template('test_methods.html', values=test_methods_dict, name="a")
# #
# #
# # def do_delete(value):
# #     """
# #     Delete values from test_methods_dict
# #     :param value:
# #     :return:
# #     """
# #     for i, elem in enumerate(test_methods_dict):
# #         if elem == value:
# #             test_methods_dict.pop(i)




@app.route("/test_methods")
@app.route("/test_methods/<strin:value>", methods=["GET", "POST", "DELETE"])
def test_methods(value=None):
    if value





if __name__ == "__main__":
    app.run()            # export FlASK_ENV=development   - режим дебагинга, код можно обновлять не перегружая сервер
