from flask import Flask, request, render_template, redirect

app = Flask(__name__)

                    #Adding a home route

@app.route('/')
def home():
    return render_template("index.html")

                    #Basics

@app.route("/basics")
def basics():
    projects = [
        {"name": "Input Output", "route": "input_output"},
        {"name": "Number Guessing Game", "route": "number_guess"},
        {"name": "Odd even", "route": "odd_even"}
    ]
    return render_template("category.html", title="Basics", projects = projects)

                    #Conditionals

@app.route("/conditionals")
def conditionals():
    projects = [
        {"name": "BMI Calculator", "route": "bmi_calculator"},
        {"name": "Calculator", "route": "calculator"},
        {"name": "Grade Calculator", "route": "grade_calculator"},
        {"name": "Ticket Pricing", "route": "ticket_pricing"}
    ]
    return render_template("category.html", title="Conditionals", projects = projects)

                    #Data Structures

@app.route("/data_structures")
def data_structures():
    projects = [
        {"name": "Dictionary phonebook", "route": "dictionary_phonebook"},
        {"name": "List Manager", "route": "list_manager"},
        {"name": "Set Operations", "route": "set_operations"},
        {"name": "String Tools", "route": "string_tools"}
    ]
    return render_template("category.html", title="Data Structures", projects = projects)

                    #Loops

@app.route("/loops")
def loops():
    projects = [
        {"name": "Pattern Printer", "route": "pattern_printer"},
        {"name": "Prime Checker", "route": "prime_checker"}
    ]
    return render_template("category.html", title="Loops", projects = projects)

                    #Functions

@app.route("/functions_page")
def functions_page():
    projects = [
        {"name": "ATM Simulator","route": "atm_simulator"},
        {"name": "Unit Converter", "route": "unit_converter"}
    ]
    return render_template("category.html", title="Functions", projects = projects)

                    #Hardcoding Routes for these mini projects
    ###BASICS###

@app.route("/input_output")
def input_output():
    return render_template("input_output.html")

@app.route("/number_guess")
def number_guess():
    return render_template("number_guess.html")

@app.route("/odd_even")
def odd_even():
    return render_template("odd_even.html")

    ###CONDITIONALS###

@app.route("/bmi_calculator")
def bmi_calculator():
    return render_template("bmi_calculator.html")

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/grade_calculator")
def grade_calculator():
    return render_template("grade_calculator.html")

@app.route("/ticket_pricing")
def ticket_pricing():
    return render_template("ticket_pricing.html")

    ###DATA STRUCTURES###

@app.route("/dictionary_phonebook")
def dictionary_phonebook():
    return render_template("dictionary_phonebook.html")

@app.route("/list_manager")
def list_manager():
    return render_template("list_manager.html")

@app.route("/set_operations")
def set_operations():
    return render_template("set_operations.html")

@app.route("/string_tools")
def string_tools():
    return render_template("string_tools.html")

    ###FUNCTIONS###

@app.route("/atm_simulator")
def atm_simulator():
    return render_template("atm_simulator.html")

@app.route("/unit_converter")
def unit_converter():
    return render_template("unit_converter.html")

    ###LOOPS###

@app.route("/pattern_printer")
def pattern_printer():
    return render_template("pattern_printer.html")

@app.route("/prime_checker")
def prime_checker():
    return render_template("prime_checker.html")


if __name__ == "__main__":
    app.run(debug=True)

