# HTTP Methods:
# Данные с вэб страниц клиента отправляются на сервер как глобальный объект request.
# Для того, чтобы работать с данными запросо request object
# должен быть импортирован из библиотеки flask.
# request.method - аттрибут method возвращает текущий метод запроса.


from flask import Flask, render_template, request

app = Flask(__name__)

data_base = ["Value1", "Value2"]  # данный список имитирует базу данных

# Составляем функции, которые аналогичные методам get, delete, post

@app.route("/")
def base():
    return "It's base_page"



def do_get():
    return render_template("test_methods.html", values=data_base)  #  в шаблоне выводятся элементы списка.



def do_delete(value):
    if value in data_base:
        data_base.remove(value)

# def do_delete(value):
#     """
#     Delete values from test_methods_dict
#     :param value:
#     :return:
#     """
#     for i, elem in enumerate(test_methods):  # enumerate -  returns tupple list [(0, value1), (1, value2)]
#         if elem == value:
#             test_methods.pop(i)






def do_post(value):
    data_base.append(value)
    return data_base


# def do_post(value):
#     """
#     This method will add value to the test_methods_dict
#     :return:
#     """
#     return test_methods.append(value)



# 2) Cоставляем функцию представления с 2-мя декораторами (данные вводяться или нет).

@app.route("/test_methods")
@app.route("/test_methods/<string:value>", methods=['GET', 'POST', 'DELETE'])
def test_methods(value=None):
    if request.method == "POST":
        do_post(value)
        return "Succcessfully added new value"
    elif request.method == "DELETE":
        do_delete(value)
        return "Successfully deleted the value"
    else:
        return do_get()



if __name__ == "__main__":
    app.run()            # export FlASK_ENV=development   - режим дебагинга, код можно обновлять не перегружая сервер


