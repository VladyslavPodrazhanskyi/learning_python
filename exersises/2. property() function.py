class person:
    def __init__(self, name="Guest"):
        self.__name=name
    def setname(self, name):          # assigns the value to the __name attribute.
       self.__name=name
    def getname(self):                # returns the value of the private instance attribute __name
       return self.__name

p1 = person('Kolya')
p1.setname('Vasya')
print(p1.getname())