amount = int(   input("Enter amount : ")    )
note_100 = amount//100
amount %= 100
note_50 = amount//50
amount %= 50
note_10 = amount//10
amount %= 10
note_5 = amount//5
amount %= 5
note_1 = amount//1
print("The no. of 100$ notes is : ", note_100)
print("The no. of 50$ notes is : ", note_50)
print("The no. of 10$ notes is : ", note_10)
print("The no. of 5$ notes is : ", note_5)
print("The no. of 1$ notes is : ", note_1)