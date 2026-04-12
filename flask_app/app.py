from flask import Flask, request, render_template
import random

app = Flask(__name__)

def truncate(number, places):
    factor = 10 ** places
    return int(number * factor) / factor

                    #Adding a home route

@app.route('/')
def home():
    return render_template("index.html")

    # Assigning URLs for the specific logics #

                    #Basics

@app.route("/basics")
def basics():
    projects = [
        {"name": "input_output", "route": "input_output"},
        {"name": "number_guess", "route": "number_guess"},
        {"name": "odd_even", "route": "odd_even"}
    ]
    return render_template("category.html", title="Basics", projects = projects)

                    #Conditionals

@app.route("/conditionals")
def conditionals():
    projects = [
        {"name": "bmi_calculator", "route": "bmi_calculator"},
        {"name": "calculator", "route": "calculator"},
        {"name": "grade_calculator", "route": "grade_calculator"},
        {"name": "ticket_pricing", "route": "ticket_pricing"}
    ]
    return render_template("category.html", title="Conditionals", projects = projects)

                    #Data Structures

@app.route("/data_structures")
def data_structures():
    projects = [
        {"name": "dictionary_phonebook", "route": "dictionary_phonebook"},
        {"name": "list_manager", "route": "list_manager"},
        {"name": "set_operations", "route": "set_operations"},
        {"name": "string_tools", "route": "string_tools"}
    ]
    return render_template("category.html", title="Data Structures", projects = projects)

                    #Loops

@app.route("/loops")
def loops():
    projects = [
        {"name": "pattern_printer", "route": "pattern_printer"},
        {"name": "prime_checker", "route": "prime_checker"}
    ]
    return render_template("category.html", title="Loops", projects = projects)

                    #Functions

@app.route("/functions_page")
def functions_page():
    projects = [
        {"name": "atm_simulator","route": "atm_simulator"},
        {"name": "unit_converter", "route": "unit_converter"}
    ]
    return render_template("category.html", title="Functions", projects = projects)

                    #Hardcoding Routes for these mini projects
    ###BASICS###

@app.route("/input_output", methods=["GET", "POST"])
def input_output():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        city = request.form["city"]

        result = f"Hello {name}! You are {age} years old and live in {city}."

    return render_template("basics/input_output.html", result=result)
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/number_guess", methods=["GET", "POST"])
def number_guess():
    result = None

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            choice = request.form["choice"]

            secret_number = random.randint(1, 10)

            if guess == secret_number:
                result = "Correct!"
            elif guess > secret_number:
                result = "Too High!"
            else:
                result = "Too Low!"

            if choice.lower() == "y":
                result += f" The correct number was {secret_number}"
            else:
                result += " Good Guess!"

        except ValueError:
            result = "Please enter a Valid Input."


    return render_template("basics/number_guess.html", result=result)
# ----------------------------------------------------------------------------------------------------------------------
@app.route("/odd_even", methods=["GET", "POST"])
def odd_even():
    result = None

    if request.method == "POST":
        try:
            number = float(request.form["number"])
            places = int(request.form["places"])

            remainder = number % 2

            if remainder == 0:
                result = f"{number} is an even number."
            else:
                truncated = truncate(remainder, places)
                result = f"{number} is an odd number. Remainder: {truncated}"


        except ValueError:
            result = "Invalid input"

    return render_template("basics/odd_even.html", result=result)

    ###CONDITIONALS###

@app.route("/bmi_calculator", methods=["GET", "POST"])
def bmi_calculator():
    result = None
    category = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            places = int(request.form["places"])

            height_m = height / 100
            bmi = weight / (height_m ** 2)

            bmi_value = truncate(bmi, places)

            if bmi <= 18.5:
                category = "Under-weight"
            elif 18.5 <= bmi <= 24.9:
                category = "Normal-weight"
            elif 25.0 <= bmi <= 29.9:
                category = "Over-weight"
            else:
                category = "Obese"

            result = f"BMI: {bmi_value}"

        except ValueError:
            result = "Invalid input"

    return render_template("conditionals/bmi_calculator.html", result=result, category=category)
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = int(request.form["operation"])
            places = int(request.form["places"])

            match operation:
                case 1:
                    result = f"Addition: {a} + {b} = {a + b}"
                case 2:
                    result = f"Subtraction: {a} - {b} = {a - b}"
                case 3:
                    result = f"Multiplication: {a} * {b} = {a * b}"
                case 4:
                    try:
                        value = a / b
                        value = truncate(value, places)
                        result = f"Division: {a} / {b} = {value}"
                    except ZeroDivisionError:
                        result = "Can't divide by zero!"
                case _:
                    result = "Invalid operation selected!"

        except ValueError:
            result = "Invalid input"

    return render_template("conditionals/calculator.html", result=result)
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/grade_calculator", methods=["GET", "POST"])
def grade_calculator():
    result = None
    grade_letter = None

    if request.method == "POST":
        try:
            pe = float(request.form["pe"])
            tn = float(request.form["tn"])
            places = int(request.form["places"])

            grade = (pe / tn) * 100
            truncated_grade = truncate(grade, places)

            if grade >= 90:
                grade_letter = "A"
            elif grade >= 75:
                grade_letter = "B"
            elif grade >= 60:
                grade_letter = "C"
            else:
                grade_letter = "Fail! Re-attempt."

            result = f"Grade: {truncated_grade}%"

        except ZeroDivisionError:
            result = "Total points cannot be zero!"
        except ValueError:
            result = "Invalid input"

    return render_template("conditionals/grade_calculator.html", result=result, grade_letter=grade_letter)
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/ticket_pricing", methods=["GET", "POST"])
def ticket_pricing():
    result = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            age = int(request.form["age"])

            if age < 12:
                price = 100
            elif 12 < age < 60:
                price = 200
            else:
                price = 120

            result = f"{name}, your ticket price is ₹{price}."

        except ValueError:
            result = "Invalid input"
    return render_template("conditionals/ticket_pricing.html", result=result)

    ###DATA STRUCTURES###
phonebook = {} #global storage
@app.route("/dictionary_phonebook", methods=["GET", "POST"])
def dictionary_phonebook():
    message = None
    search_result = None

    if request.method == "POST":
        action = request.form["action"]

        # Add contact
        if action == "add":
            name = request.form["name"]
            number = request.form["number"]
            phonebook[name] = number
            message = "Contact Added!"

        # Search contact
        elif action == "search":
            name = request.form["search_name"]
            if name in phonebook:
                search_result = f"{name}'s number is {phonebook[name]}"
            else:
                search_result = "Contact not found!"

        #Delete a contact
        elif action == "delete":
            name = request.form["delete_name"]
            if name in phonebook:
                del phonebook[name]
                message = f"{name} deleted!"
            else:
                message = "Contact not found!"

    return render_template("data_structures/dictionary_phonebook.html",
                           phonebook=phonebook, message=message, search_result=search_result)
#-----------------------------------------------------------------------------------------------------------------------
items = []  #global list
@app.route("/list_manager", methods=["GET", "POST"])
def list_manager():
    message = None

    if request.method == "POST":
        action = request.form["action"]

        # Add item
        if action == "add":
            item = request.form["item"]
            items.append(item)
            message = f"{item} added!"

        # Remove item
        elif action == "remove":
            item = request.form["remove_item"]
            if item in items:
                items.remove(item)
                message = "Item removed!"
            else:
                message = "Item not found!"

    return render_template("data_structures/list_manager.html", items=items,
        message=message)
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/set_operations", methods=["GET", "POST"])
def set_operations():
    union = None
    intersection = None
    difference = None
    error = None

    if request.method == "POST":
        try:
            set1 = set(map(int, request.form["set1"].split()))
            set2 = set(map(int, request.form["set2"].split()))

            union = set1 | set2
            intersection = set1 & set2
            difference = set1 - set2

        except ValueError:
            error = "Please enter valid numbers separated by spaces."

    return render_template("data_structures/set_operations.html",
    union=union, intersection=intersection, difference=difference, error=error)
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/string_tools",  methods=["GET", "POST"])
def string_tools():
    length = None
    upper = None
    reversed_str = None

    if request.method == "POST":
        s = request.form["text"]

        length = len(s)
        upper = s.upper()
        reversed_str = s[::-1]

    return render_template("data_structures/string_tools.html",
    length=length, upper=upper, reversed=reversed_str)

    ###FUNCTIONS###

balance = 10000  # global balance

@app.route("/atm_simulator", methods=["GET", "POST"])
def atm_simulator():
    global balance
    message = None

    if request.method == "POST":
        action = request.form["action"]

        if action == "check":
            message = f"Current Balance: ₹{balance}"

        elif action == "deposit":
            try:
                amount = float(request.form["amount"])
                balance += amount
                message = f"₹{amount} deposited successfully."
            except ValueError:
                message = "Invalid amount"

        elif action == "withdraw":
            try:
                amount = float(request.form["amount"])
                if amount > balance:
                    message = "Insufficient balance!"
                else:
                    balance -= amount
                    message = f"₹{amount} withdrawn successfully."
            except ValueError:
                message = "Invalid amount"

    return render_template("functions_page/atm_simulator.html",  balance=balance, message=message)
#-----------------------------------------------------------------------------------------------------------------------
def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

@app.route("/unit_converter", methods=["GET", "POST"])
def unit_converter():
    result = None

    if request.method == "POST":
        try:
            choice = request.form["choice"]
            value = float(request.form["value"])

            if choice == "km_to_miles":
                converted = km_to_miles(value)
                result = f"{value} km = {converted:.2f} miles"

            elif choice == "c_to_f":
                converted = celsius_to_fahrenheit(value)
                result = f"{value}°C = {converted:.2f}°F"

            else:
                result = "Invalid choice!"

        except ValueError:
            result = "Invalid input"
    return render_template("functions_page/unit_converter.html", result=result)

    ###LOOPS###

@app.route("/pattern_printer", methods=["GET", "POST"])
def pattern_printer():
    pattern = None
    error = None

    if request.method == "POST":
        try:
            x = int(request.form["rows"])

            if x <= 0:
                error = "Please enter a positive number."
            else:
                lines = []

                # Upper half
                for i in range(1, x + 1):
                    spaces = " " * (x - i)
                    stars = "*" * (2 * i - 1)
                    lines.append(spaces + stars)

                # Lower half
                for j in range(x - 1, 0, -1):
                    spaces = " " * (x - j)
                    stars = "*" * (2 * j - 1)
                    lines.append(spaces + stars)

                pattern = "\n".join(lines)

        except ValueError:
            error = "Invalid input"
    return render_template("loops/pattern_printer.html", pattern=pattern, error=error)
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/prime_checker", methods=["GET", "POST"])
def prime_checker():
    result = None

    if request.method == "POST":
        try:
            number = int(request.form["number"])

            if number <= 1:
                result = "This number is not prime. Enter a positive integer."
            else:
                for i in range(2, number):
                    if number % i == 0:
                        result = "Not a prime number"
                        break
                else:
                    result = "Prime number"

        except ValueError:
            result = "Invalid input"
    return render_template("loops/prime_checker.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)

