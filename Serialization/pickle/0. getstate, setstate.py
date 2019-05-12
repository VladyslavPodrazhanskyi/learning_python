class Cat:
  def __init__(self, age=2):
     self.age = age

  def __getstate__(self):
     self.age *= 2       # you can change object_dict here
     return self.__dict__   # object dict - key-attribut, value - its value

  # def __setstate__(self, d):
  #    print("I'm being unpickled with these values:", d)
  #    self.__dict__ = d
  #    self.number *= 3

import pickle
f = Cat()
print(f)
print(f.__getstate__())
f_string = pickle.dumps(f)
f_new = pickle.loads(f_string)
print(f.age)
print(f_new.age)