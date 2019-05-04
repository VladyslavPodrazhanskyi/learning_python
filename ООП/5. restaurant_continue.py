# 9-1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant дол-
# жен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод describe_
# restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит
# сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по
# отдельности, затем вызовите оба метода.
# 9-2. Три ресторана: начните с класса из упражнения 9-1. Создайте три разных экземпляра,
# вызовите для каждого экземпляра метод describe_restaurant().
# 9-4. Посетители: начните с программы из упражнения 9-1 (с.  165). Добавьте атрибут
# number_served со значением по умолчанию 0; он представляет количество обслуженных
# посетителей. Создайте экземпляр с именем restaurant. Выведите значение number_served,
# потом измените и выведите снова.
# Добавьте метод с именем set_number_served(), позволяющий задать количество обслужен-
# ных посетителей. Вызовите метод с новым числом, снова выведите значение.
# Добавьте метод с именем increment_number_served(), который увеличивает количество
# обслуженных посетителей на заданную величину. Вызовите этот метод с любым числом,
# которое могло бы представлять количество обслуженных клиентов — скажем, за один день.


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        print("Restaurant " + restaurant_name.title() + " is created!")


    def describe_restaurant(self):
        print(self.restaurant_name.title() + ", " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opened!")
    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers
    def increment_number_served(self, new_served):
        if new_served >= 0:
            self.number_served += new_served
        else:
            print("You are not able to reduct number_served!")



rest1 = Restaurant("Utopia", "American food")
print(rest1.restaurant_name)
print(rest1.cuisine_type)
rest1.describe_restaurant()
rest1.open_restaurant()

rest2 = Restaurant("Mafia", "Italian food")
rest2.describe_restaurant()

print(rest2.number_served)
rest2.number_served = 324
print(rest2.number_served)
rest2.increment_number_served(45)
print(rest2.number_served)

rest3 = Restaurant("Eastern Star", "Chinese food")
rest3.describe_restaurant()
print(rest3.number_served)
rest3.set_number_served(567)
print(rest3.number_served)