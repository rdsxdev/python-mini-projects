from utils.dec_truncate import truncate
#Getting an input from user
number = float(input("Enter a number: "))

#Calculate the remainder
remainder = number % 2

#Check for the remainder when the number is divided by 2
if remainder == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#Printing the Remainder
print(truncate(f"Remainder when divided by 2: {remainder}"))
