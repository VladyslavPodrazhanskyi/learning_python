# Киоск с мороженым: киоск с мороженым — особая разновидность ресторана.
# Напишите класс IceCreamStand, наследующий от класса Restaurant
# Добавьте атрибут с именем flavors для хранения списка сортов мороженого.
# Напишите метод, который выводит этот список.
# Создайте экземпляр IceCreamStand  и вызовите этот метод.



class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0



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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="ice_cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["strawberry_pleasure", "juice_ice", "chocolate_ecstasy"]
    def display_flavors(self):
        print("You can buy following ice creams here:")
        for flavor in self.flavors:
            print(flavor.title())

my_favorite_icecream_stand = IceCreamStand("SuperIce")
my_favorite_icecream_stand.display_flavors()
my_favorite_icecream_stand.increment_number_served(437)
print(my_favorite_icecream_stand.number_served)
