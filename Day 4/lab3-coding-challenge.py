import random

names = input("Give me everybosy's names, seperated by a comma. ")

names = names.split(". ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person = names[random_choice]

print(person + " is going to buy the meal today.")
