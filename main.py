from resources import *

print("Welcome")
while True:
    choice = input("Would you like to continue? (yes/no): ")
    if choice == "no":
        print("Okay, Bye!")
        quit()

    print("Please Choose What you'd like to calculate")
    print("1.Carrier Rocket")
    print("2.Universe Matrix")
    print("3.Other")

    choice = int(input("input your choice: "))

    while choice != 1 and choice != 2 and choice != 3:
        choice = input("Wrong Value, try again: ")

    if choice == 3:
        name = input("Please enter the name of the resource you'd like to calculate: ")
        name = name.lower()
        name = name.title()


    number = int(input("Alright, Now enter the amount you would like to manufacture: "))

    if choice == 1:
        if cost != {}:
            clear = input("Do you want to clear the existing cost? (yes/no): ")
            if clear == "yes":
                cost.clear()
        parts = carrier_rocket.cost_calc(number)
        for key in parts.keys():
            print(key, parts.get(key))

    elif choice == 2:
        if cost != {}:
            clear = input("Do you want to clear the existing cost? (yes/no): ")
            if clear == "yes":
                cost.clear()
        parts = matrix_unify.cost_calc(number)
        for key in parts.keys():
            print(key, parts.get(key))

    elif choice == 3:
        parts = dict()
        if cost != {}:
            clear = input("Do you want to clear the existing cost? (yes/no): ")
            if clear == "yes":
                cost.clear()
        for index in all_parts:
            if name == index.name:
                parts = index.cost_calc(number)
                break
        for key in parts.keys():
            print(key, parts.get(key))
