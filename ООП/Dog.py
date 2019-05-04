Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Dog:
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
