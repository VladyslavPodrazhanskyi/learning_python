# 1)Обязательная агрегация class Person inside class Horse as rider
# 2) Вызов метода внутреннего класса Person из внешнего класса Horse
class Person:
    def __init__(self, name):
        self.name = name
    def owner_feeds(self):
        print(f"Owner {self.name} is feeding his horse!")

class Horse:
    def __init__ (self,
                  name,
                  breed,
                  age):
        self.name = name
        self.breed = breed
        self.age = age
        self.rider = Person('Vlad')
        print('Horse created') 


current_horse = Horse('Favorite',
                      'Campolina',
                      7)
print(current_horse.rider.name)
print(current_horse.rider)
current_horse.rider.name = "Igor"
print(current_horse.rider)           # даже при смене имени объект rider не изменился, изменилось только его имя.
current_horse.rider.owner_feeds()
                      
                      

        
