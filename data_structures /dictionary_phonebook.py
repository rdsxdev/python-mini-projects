phonebook = {}

while True:
    print("\nPhonebook Menu")
    print("(1) Add Contacts")
    print("(2) Search Contacts")
    print("(3) Display All Contacts")
    print("(4) Exit")

    choice = input("Enter your choice: ")

    #Add contacts
    if choice == "1":
        name = input("Enter your name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact Added!")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phonebook:
            print(f"{name}' number is {phonebook[name]}")
        else:
            print("Contact not found!")

    #Display all the contacts
    elif choice == "3":
        if phonebook:
            print("\nAll Contacts:")
            for name, number in phonebook.items():
                print(name, ":", number)
        else:
            print("Phonebook is empty.")

    #Exit
    elif choice == "4":
        print("Exiting phonebook.")
        break
    else:
        print("Invalid choice.")
