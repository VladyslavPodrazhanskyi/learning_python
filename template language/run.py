from flask import Flask, render_template  # rendering html templates

app = Flask(__name__)  # creation of flask application


@app.route("/")      # декоратор позволяет задать путь в котором будет размещаться шаблон
def start():
    return render_template('update_template.html', my_string="Start!", my_list=[0,1,2,3,4,5], title="Start")


@app.route("/home")
def home():
    return render_template('update_template.html', my_string="Home!", my_list=[0,1,2,3,4,5], title="Home")

@app.route("/about")
def about():
    return render_template('update_template.html', my_string="About!", my_list=[0,1,2,3,4,5], title="About")

@app.route("/contact")
def contact():
    return render_template('update_template.html', my_string="Contact us!", my_list=[0,1,2,3,4,5], title="Contact Us")

@app.route("/newlink")
def newlink():
    return render_template('update_template.html', my_string="new link!", my_list=[0,1,2,3,4,5], title="new link")



if __name__ == '__main__':
    app.run(debug=True)     # запуск вэб приложения.
