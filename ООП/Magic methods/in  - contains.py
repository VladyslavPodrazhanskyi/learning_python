

models = ("Skoda", "Lada", "Toyota", "Ford", "Lexus")
towns = ("Rome", "Kiev", "Riga", "Boston", "London")

class Car:
    def __init__(self, number, model, year):
        self.number = number
        self.model = model
        self.year = year

cars = []
for i in range(20):
    cars.append(Car(uuid.uuid4(), random.choice(models), random.randrange(1980, 2018)))

# pprint.pprint(cars)




class Garage:
    def __init__(self, number, town, places):
        self.number = number
        self.town =  town
        self.places = places
        self.cars = cars if cars is not None else []


    def __contains__(self, item):
        return item in self.members




my_garage = Garage(uuid.uuid4(), random.choice(towns), 20)
my_garage.cars = cars
# print(my_garage.number)

for car in my_garage:
    print(car)


print(<__main__.Car object at 0x7f987e9ff940> in my_garage)