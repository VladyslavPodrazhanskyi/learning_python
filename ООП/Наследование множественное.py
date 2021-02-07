class Animal:
    def __init__(self, age):
        self.age = age

    def run(self):
        return "run"


class Bird:
    def fly(self):
        return "I can fly"

    def run(self):
        return "I can't run"


class RunningBird(Animal, Bird): # при множеств. наследии в приоритете 1 родитель
    def run(self):
        return super().run()

rb = RunningBird(14)

print(rb.run())     # run
print(rb.fly())     # I can fly