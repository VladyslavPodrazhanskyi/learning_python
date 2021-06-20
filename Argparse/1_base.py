import argparse
parser = argparse.ArgumentParser()  # of экземпляр класса
parser.add_argument("square", help="display a square of a given number", type=int)        # принимаемый аргумент
args = parser.parse_args()         # сохранение аргументов в пер. args
print(args.square**2)                   # вывод на печать аргументы
