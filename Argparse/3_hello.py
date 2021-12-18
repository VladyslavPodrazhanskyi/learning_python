import argparse
parser = argparse.ArgumentParser()  # of экземпляр класса
parser.add_argument("greeting")        # принимаемый аргумент
parser.add_argument("name", help="name for greeting")        # принимаемый аргумент



def format_greeting(greeting, name):
    return f"{greeting.title()}, {name.title()}!"


if __name__ == '__main__':
    args = parser.parse_args()   # сохранение аргументов в переменной args
    name = args.name
    greeting = args.greeting
    print(format_greeting(greeting, name))
