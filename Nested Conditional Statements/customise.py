print("Which ride do you want to take : ")
print("1. Car")
print("2. Bike")

choice = int(input("Enter your choice : "))
if choice == 1:
    print("Select your car : ")
    print("1. BMW")
    print("2. SUV")
    choice_car = int(input("Enter your choice : "))
    if choice_car == 1:
        print("You have selected BMW")
    else:
        print("You have selected SUV")


elif choice == 2:
    print("Select your bike : ")
    print("1. Honda")
    print("2. Hero")
    choice_bike = int(input("Enter your choice : "))
    if choice_bike == 1:
        print("You have selected Honda")
    else:
        print("You have selected Hero")


else:
    print("Incorrect choice")        