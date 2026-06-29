# Take input from the user
medical_cause = input("Did you have a medical cause? (Y/N)  ").strip().upper()
if medical_cause == 'Y':
    print("You are alllowed. ")
else:
    attnd = int(input("Enter your attendance : "))
    if attnd >= 75:
        print("You are allowed.")
    else:
        print("You are not allowed.") 
    
    