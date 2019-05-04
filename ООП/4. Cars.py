# 9-3. Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_
# name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользова-
# теля. Напишите метод describe_user(), который выводит сводку с информацией о пользо-
# вателе. Создайте еще один метод greet_user() для вывода персонального приветствия для
# пользователя.
# Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба
# метода для каждого пользователя.

class User():
    def __init__(self, first_name, last_name, nick_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.age = age
        self.email = email
    def describe_user(self):
        print("Current user's first name is {}, last name is {}, age is {} years old.".format(self.first_name,
            self.last_name, self.age))
    def greet_user(self):
        print("Hello, Dear " + self.first_name.title() + " " + self.last_name.title() + "!")

user1 = User("Vladislav", "Podrazhanskyi", "Dostigator", 39, "vladislav304304@gmail.com")
user1.describe_user()
user1.greet_user()