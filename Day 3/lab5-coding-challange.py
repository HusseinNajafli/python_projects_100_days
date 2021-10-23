# Love Calculator

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

# t, r, u, e, l, o, v

true_score = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love_score = name.count("l") + name.count("o") + name.count("v") + name.count("e")

score = int(str(true_score) + str(love_score))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
