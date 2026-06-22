height = float(input("Enter Your Height in metres : "))
weight = float(input("Enter Your Weight in kg : "))
BMI = weight / (height) **2
if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("You are obese")
else: 
    print("You are severely obese")        


