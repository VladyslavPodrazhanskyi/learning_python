# 9-1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant дол-
# жен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод describe_
# restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит
# сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по
# отдельности, затем вызовите оба метода.
# 9-2. Три ресторана: начните с класса из упражнения 9-1. Создайте три разных экземпляра,
# вызовите для каждого экземпляра метод describe_restaurant().


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        print("Restaurant " + restaurant_name.title() + " is created!")

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ", " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opened!")

rest1 = Restaurant("Utopia", "American food")
print(rest1.restaurant_name)
print(rest1.cuisine_type)
rest1.describe_restaurant()
rest1.open_restaurant()

rest2 = Restaurant("Mafia", "Italian food")
rest3 = Restaurant("Eastern Star", "Chinese food")

rest2.describe_restaurant()
rest3.describe_restaurant()