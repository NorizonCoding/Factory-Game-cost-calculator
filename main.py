from resources import *

print("Welcome")
print("Please Choose What you'd like to calculate")
print("1.Carrier Rocket")
print("2.Universe Matrix")
print("3.Other")
print("Type anything else to Exit")
choice = int(input("input your choice: "))

if choice != 1 and choice != 2 and choice != 3:
    print("Aight, have a nice day!")
    quit()

number = int(input("Alright, Now enter the amount you would like to manufacture: "))

if choice == 1:
    parts = carrier_rocket.cost_calc(number)
    for key in parts.keys():
        print(key, parts.get(key))
