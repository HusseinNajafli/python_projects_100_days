# Pizza Order Practice - Dr.Angela Yu

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extre cheese? Y or N: ")

bill = 0

# Size condition
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# Pepperoni condition
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Cheese condition
if extra_cheese == "Y":
    bill += 1
    
print(f"Your total bill is: ${bill}")
