#switching variables values

a = input("a: ")
b = input("b: ")

#define temporary value for keep our values

#for example a = 3, b = 5

temp = a
#temp = 3
a = b
#a = 5
b = temp
#b = 3

print("a: " + a)
print("b: " + b)