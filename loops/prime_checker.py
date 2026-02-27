number = int(input("Enter a number: "))

if number <= 1:
    print("This number is not prime. Enter a postive integer.")

else:
    #To check if its prime
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number")
            break

    else:
        print("Prime number")