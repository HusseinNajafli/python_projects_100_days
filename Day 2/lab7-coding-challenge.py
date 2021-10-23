print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))

people = int(input("How many people to split the bill? "))

total_bill = round((bill + ((bill * tip) / 100)) / people, 2)
total_bill = "{:.2f}".format(total_bill)

print(f"Each person should pay: ${total_bill}")