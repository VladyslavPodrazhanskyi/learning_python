import time

class Calculator:
    def summ(self, a, b):
        time.sleep(10)
        return a + b


myc = Calculator()

if __name__ == '__main__':
    print(myc.summ(5, 6))
