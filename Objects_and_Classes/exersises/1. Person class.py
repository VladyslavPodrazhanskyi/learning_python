
class Person():

    greet = "Hello"                   # class attribute
    total_quantity = 0

    def __init__(self, name, age):    # class constructor
        self.name = name              # instance attribute
        self.age = age
        Person.total_quantity += 1    # change of class attribute when new instance is created

    def display_info(self):           # instance method
        print(self.name, self.age)


p1 = Person('Mike', '25')                # creation of 1st instance
p2 = Person('Nick', '18')                # creation of 2nd instance

print(Person.greet)                      # show class attribut greet
p1.greet = "By"                          # changed class attribute greet for instance p1
print(Person.greet)                      # show class attribute greet for Class (is wasn't changed)
print(p1.greet)                          # show class attribute greet for p1 ( it was changed)

Person.greet = "I on the vacation"        # change class attribute greet
print(p1.greet)                           # class attribute for instance p1 left the same
print(p2.greet)
print(Person.total_quantity)              # show class attribute total quantity
print(p1.total_quantity)                  # class attribute for instance p2 was changed

p1.display_info()                         # use method display_info for instance p1
p2.display_info()