# -------- FUNCTIONS --------

def km_to_miles(km):
    return km * 0.621371


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


# -------- MENU --------

while True:
    print("\nUnit Converter")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km_to_miles(km)
        print(f"{km} km = {miles:.2f} miles")

    elif choice == "2":
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f:.2f}°F")

    elif choice == "3":
        print("Exiting converter.")
        break

    else:
        print("Invalid choice!")