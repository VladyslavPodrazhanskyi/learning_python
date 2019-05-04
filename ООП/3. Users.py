# 9-3. Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_
# name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользова-
# теля. Напишите метод describe_user(), который выводит сводку с информацией о пользо-
# вателе. Создайте еще один метод greet_user() для вывода персонального приветствия для
# пользователя.
# Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба
# метода для каждого пользователя.
# 9-5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9-3
# (с.  165). Напишите метод increment_login_attempts(), увеличивающий значение login_
# attempts на 1. Напишите другой метод с именем reset_login_attempts(), обнуляющий значе-
# ние login_attempts.
# Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз. Вы-
# ведите значение login_attempts, чтобы убедиться в том, что значение было изменено пра-
# вильно, а затем вызовите reset_login_attempts(). Снова выведите login_attempts и убеди-
# тесь в том, что значение обнулилось.

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
