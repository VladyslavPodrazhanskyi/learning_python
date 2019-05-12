def divide_num(num1, num2):
    try:
        res = num1/num2
    except ZeroDivisionError:
        print("You cannot divide on Zero")
    else:
        message = f"{num1} divided on {num2} is equal to {res}."
        print(message)



while True:
    print("Give me 2 number and I divide them.")
    print("Plese enter 'q' to quit.")
    input1 = input("Input number1: ")
    if input1 == "q":
        break
    while True:
        try:
            num1 = float(input1)
        except ValueError:
            input1 = input("Input number1: ")
            continue
        else:
            break

    input2 = input("Input number2: ")
    if input2 == "q":
        break
    while True:
        try:
            num2 = float(input2)
        except ValueError:
            input2 = input("Input number2: ")
            continue
        else:
            break
    divide_num(num1, num2)
