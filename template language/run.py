import datetime

from flask import Flask, render_template  # rendering html templates

app = Flask(__name__)  # creation of flask application

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route("/")      # декоратор позволяет задать путь в котором будет размещаться шаблон
def start():
    return render_template('update_template.html', my_string="Start!", my_list=[0,1,2,3,4,5], title="Start",
                           current_time=datetime.datetime.now())


@app.route("/home")
def home():
    return render_template('update_template.html', my_string="Home!", my_list=[0,1,2,3,4,5], title="Home",
                           current_time=datetime.datetime.now())

@app.route("/about")
def about():
    return render_template('update_template.html', my_string="About!", my_list=[0,1,2,3,4,5], title="About",
                           current_time=datetime.datetime.now())

@app.route("/contact")
def contact():
    return render_template('update_template.html', my_string="Contact us!", my_list=[0,1,2,3,4,5], title="Contact Us",
                           current_time=datetime.datetime.now())

@app.route("/newlink")
def newlink():
    return render_template('update_template.html', my_string="new link!", my_list=[0,1,2,3,4,5], title="new link",
                           current_time=datetime.datetime.now())



if __name__ == '__main__':
    app.run(debug=True)     # запуск вэб приложения.
