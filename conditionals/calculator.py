from utils.dec_truncate import truncate
#Input for users
a = float(input("Select a digit(1):"))
b = float(input("Select a digit(2):"))

#Selection of an operation
print(
    "Select an operation to be performed:\n"
    "(1)Addition\n"
    "(2)Subtraction\n"
    "(3)Multiplication\n"
    "(4)Division"
)
c = int(input("Enter the number:"))

#In Python we have match-case for the replacement of switch cases
number = c
match number:
    case 1:
        print(f"Addition: {a} + {b} = {a + b}")
    case 2:
        print(f"Subtraction: {a} - {b} = {a - b}")
    case 3:
        print(f"Multiplication: {a} * {b} = {a * b}")

#Code exception block
    case 4:
        try:
            result = a / b
            print(truncate(f"Division: {a} / {b} = {result}"))
        except ZeroDivisionError:
            print("Can't be divided by zero!")
    case _:
        print("Invalid operation selected!")