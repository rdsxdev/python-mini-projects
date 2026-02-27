x = int(input("Enter the number of rows: "))
if x <= 0:
    print("Please enter a positive number.")
else:
    #range(start, end - 1)
    for i in range(1, x + 1):
        spaces = " " * (x - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    #range(start, stop, step)
    for j in range(x - 1 , 0, -1):
        spaces = " " * (x - j)
        stars = "*" * (2 * j - 1)
        print(spaces + stars)




