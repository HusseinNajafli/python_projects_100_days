# Sum of even numbers from 1 to 100 (including 1 and 100)

# Solution 1
sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(sum)

# Solution 2
sum1 = 0
for number in range(2, 101, 2):
    sum1 += number
print(sum1)
