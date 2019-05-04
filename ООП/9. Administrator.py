# Администратор: администратор — особая разновидность пользователя. Напишите
# класс с именем Admin, наследующий от класса User из упражнения 9-3 (с.  165) или
# упражнения 9-5 (с. 170). Добавьте атрибут privileges для хранения списка строк вида
# «разрешено добавлять сообщения», «разрешено удалять пользователей», «разрешено
# банить пользователей» и т.  д. Напишите метод show_privileges() для вывода набора
# привилегий администратора. Создайте экземпляр Admin и вызовите свой метод.
# 9-8. Привилегии: напишите класс Privileges. Класс должен содержать всего один атрибут
# privileges со списком строк из упражнения 9-7. Переместите метод show_privileges() в этот
# класс. Создайте экземпляр Privileges как атрибут класса Admin. Создайте новый экземпляр
# Admin и используйте свой метод для вывода списка привилегий.


class User():
    def __init__(self, first_name, last_name, nick_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.age = age
        self.email = email
        self.login_attempts = 0
    def describe_user(self):
        print("Current user's first name is {}, last name is {}, age is {} years old.".format(self.first_name,
            self.last_name, self.age))

    def greet_user(self):
        print("Hello, Dear " + self.first_name.title() + " " + self.last_name.title() + "!")
    def increment_login_attempts(self, current_attempts_number):
        self.login_attempts += current_attempts_number
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Vladislav", "Podrazhanskyi", "Dostigator", 39, "vladislav304304@gmail.com")
user1.describe_user()
user1.greet_user()
print(user1.login_attempts)
user1.increment_login_attempts(65)
user1.increment_login_attempts(4)
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

class Admin(User):
    def __init__(self, first_name, last_name, nick_name, age, email):
        super().__init__(first_name, last_name, nick_name, age, email)
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей"]
    def show_privileges(self):
        print("У администратора есть привелегиии: \n")
        for privilege in self.privileges:
            print(privilege.title())

our_admin = Admin("Sergey", "Gorpinko", "Jack Potroshitel", 28, "s.gorpinko@gmail.com")
our_admin.show_privileges()
our_admin.greet_user()
our_admin.describe_user()