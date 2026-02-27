#Determine ticket price based on age
name = input("Enter your name:")
age = int(input("Enter your age:"))

if age < 12:
    print(f"{name} your ticket price is ₹100.")

elif 12 < age < 60:
    print(f"{name} your ticket price is ₹200.")

else:
    print(f"{name} your ticket price is ₹120.")