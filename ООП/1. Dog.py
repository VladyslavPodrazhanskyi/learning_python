
class Dog:
    '''Простая модель собаки.'''
    def __init__(self, name, age):
        '''Инициализирует атрибуты name и age.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Собака садится по команде'''
        print(self.name.title() + " is now sitting" )
    def roll_over(self):
        '''Собака перекатывается по команде'''
        print(self.name.title() + "is rolled over!")


dog1 = Dog('Tobik', 5)
print(dog1.name, dog1.age)
dog1.sit()
dog1.roll_over()
