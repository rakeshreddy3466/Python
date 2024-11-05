# example code for nested if statements and elif statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("can ride")
    age = int(input("enter your age"))
    if age < 12:
        bill = 5
        print("you need to pay $5")
    elif (age >= 12 and age <= 18):
        bill = 7
        print("you need to pay $7")
    else:
        bill = 12
        print("you need to pay $12") 
    photo = str(input("do you want photo yes or no?"))
    if photo == "yes":
        bill += 3
        print(f"your total bill is {bill}")
else:
    print("can't ride")
