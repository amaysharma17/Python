Cost_Price = float (input("Enter Your Cost Price : "))
Selling_Price = float (input("Enter Your Selling Price : "))
if Selling_Price > Cost_Price:
    profit = Selling_Price - Cost_Price
    print(f"Profit of {Selling_Price} and {Cost_Price} is :, {profit}")
else : 
    print("You are in loss")    