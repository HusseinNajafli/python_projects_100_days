# Calculater

age = input("Input your age: ")

age = int(age)

days = 365 * (90 - age)

weeks = (90 - age) * 52
weeks = int(weeks)

months = (90 - age) * 12

print(f"You have {days} days, {weeks} weeks and {months} months left.")