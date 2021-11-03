# Python Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', ']', '[', '{', '}', ',', '.', '/', '^', '@',
           '"', '`', '~', ':', ';', '?', '|', '_', '=', "'"]
print("Welcome to the PyPassword Generator!")

letters_size = int(input("How many letters would you like in your password?\n"))
symbols_size = int(input("How many symbols would you like?\n"))
numbers_size = int(input("How many numbers would you like?\n"))

# Easy Level
password = ""
for letter in range(1, letters_size + 1):
    password += random.choice(letters)
for char in range(1, symbols_size + 1):
    password += random.choice(symbols)
for number in range(1, numbers_size + 1):
    password += random.choice(numbers)

print("My easy password is:")
print(password)