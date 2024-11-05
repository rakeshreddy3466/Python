# example code for nested if statements and elif statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("can ride")
    age = int(input("enter your age"))
    if age < 12:
        print("you need to pay $5")
    elif (age >= 12 and age <= 18):
        print("you need to pay $7")
    else:
        print("you need to pay $12") 
else:
    print("can't ride")
