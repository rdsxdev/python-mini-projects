#We need a random (1-10) picker
import random
secret_number = random.randint(1, 10)
try:
    guess = int(input("Guess a number between 1 to 10: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if guess == secret_number:
    print("Correct!")
elif guess > secret_number:
    print("Too High!")
else:
    print("Too low!")

#Taking user input
choice = input("Want to know the correct guess?(Y/n)")
if choice == "Y" or choice == "y":
    print("The correct number is:", secret_number)
else:
    print("Good Guess!")
