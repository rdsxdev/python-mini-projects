#Creating an empty list
items = []
#Keeps running until manually stopped
while True:

    print("\n Menu:")
    print("(1) Add item")
    print("(2) Remove item")
    print("(3) Display item")
    print("(4) Exit")

    #Take user choice
    choice = input("Enter choice: ")

    #Add item
    if choice == "1":
        item = input("Enter item to add:")
        items.append(item) #adds an item at the end
        print(f"{item} added!")

    #Remove item
    elif choice =="2":
        item = input("Enter items to remove:")
        #Nested if-else for error handling
        if item in items:
            items.remove(item)
            print("Item removed!")
        else:
            print("Item not Found!")

    #Display List
    elif choice == "3":
        print("Current list:", items)

    #Exit program
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")