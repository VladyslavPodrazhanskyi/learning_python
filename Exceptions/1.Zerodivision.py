def divide_num(num1, num2):
    try:
        res = float(num1)/float(num2)
    except ValueError:
        print("You should input Number, not a text")
    except ZeroDivisionError:
        print("You cannot divide on Zero")
    else:
        message = f"{num1} divided on {num2} is equal to {res}."
        print(message)


while True:
    print("Give me 2 nimbers and I divide them.")
    print("Plese enter 'q' to quit.")
    num1 = input("Input first number: ")
    if num1 == "q":
        break
    num2 = input("Input second number: ")
    if num2 == "q":
        break
    divide_num(num1, num2)
