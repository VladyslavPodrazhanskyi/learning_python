class Person:
    def __init__(self, name):
        self.name = name
    
    def sayhi(self):
        print ('Hi, my name is ', self.name+'!')
        
p = Person('Vlad')
p.sayhi()

