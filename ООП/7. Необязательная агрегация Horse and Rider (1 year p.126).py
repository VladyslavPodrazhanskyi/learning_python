class Person:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__ (self,
                  name,
                  breed,
                  age,
                  rider):
        self.name = name
        self.breed = breed
        self.age = age
        self.rider = rider
        print('Horse created') 

current_rider = Person('Vlad')
current_horse = Horse('Favorite',
                      'Campolina',
                      7,
                      current_rider)
print(current_horse.rider.name)
                      
                      

        
