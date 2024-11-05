print("Welcome to the tip calculator")
total_bill = float(input("what is the total bill "))
tip = float(input("how much tip would you like to give? 10, 12,or 15? "))
tip_totalbill = total_bill + (total_bill/100)*tip
people = int(input("how many people to spilt the bill?"))
print(f"Each person should pay: {round(tip_totalbill / people, 2)} ")