# Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extre cheese? Y or N: ")

"""
S = $15
M = $20
L = $25

Pepperoni for S: + $2
Pepperoni for M, L: + $3

Extra cheese for any size pizza: + $1
"""

S = 15
M = 20
L = 25

pepperoni_s = 2
pepperoni_m_l = 3

cheese = 1

total_bill = 0

# Pizza Order Algorithm
if size == "S":
    total_bill += 15
    if add_pepperoni == "Y":
        total_bill += pepperoni_s
    if extra_cheese == "Y":
        total_bill += cheese
    print(f"Your final bill is: ${total_bill}")
elif size == "M":
    total_bill += 20
    if add_pepperoni == "Y":
        total_bill += pepperoni_m_l
    if extra_cheese == "Y":
        total_bill += cheese
    print(f"Your final bill is: ${total_bill}")
else:
    total_bill += 25
    if add_pepperoni == "Y":
        total_bill += pepperoni_m_l
    if extra_cheese == "Y":
        total_bill += cheese
    print(f"Your final bill is: ${total_bill}")