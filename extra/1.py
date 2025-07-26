# Task 1: Write a program to calculate Body Mass Index (BMI).
# Ask the user for their weight and height, 
# then compute and display their BMI and classification.
# BMI formula: BMI = weight / (height ** 2), 
# where weight in kg and height in meters

weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = weight / (height ** 2)  # BMI calculation
print("Your BMI is: ",bmi)

# Classifying the BMI
if bmi < 18.5:
    print("Classification: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Classification: Normal weight")
elif 25 <= bmi < 29.9:
    print("Classification: Overweight")
else:
    print("Classification: Obese")


# Task 2: Compute the following expressions and 
# compare results with your class fellows and class teacher.

# Expression 1: 10 + 3*2**2 - 5/5
expr1 = 10 + 3 * 2 ** 2 - 5 / 5
print("Result of expression 1 (10 + 3*2**2 - 5/5):", expr1)

# Expression 2: (10 + 3) * (2 ** (2 - 1)) / 5
expr2 = (10 + 3) * (2 ** (2 - 1)) / 5
print("Result of expression 2 ((10 + 3) * (2 ** (2 - 1)) / 5):", expr2)


# Task 3: Translate the following in Python's syntax

# 1. 25 + 3 x 4 - 7 ** 2 + 1 → (Using * for multiplication and ** for power)
expression3 = 25 + 3 * 4 - 7 ** 2 + 1
print("Result of translated expression 1 (25 + 3*4 - 7**2 + 1):", expression3)

# 2. 210 x (2 + 3) - 4 ** 8 : 2 + 5
# Assuming ":" is intended as division
expression4 = 210 * (2 + 3) - (4 ** 8) / 2 + 5
print("Result of translated expression 2 (210*(2+3) - 4**8 / 2 + 5):", expression4)


# Task 4: Write a Python program that prints even and counts the odd numbers from 1 to 20 using a while loop

num = 1
odd_count = 0

print("Even numbers between 1 and 20:")
while num <= 20:
    if num % 2 == 0:
        print(num)  # Print even numbers
    else:
        odd_count += 1  # Count odd numbers
    num += 1

print("\nTotal odd numbers between 1 and 20:", odd_count)


# Task 5: Write a Python program that iterates 
# over a list of temperatures and
# prints “Warm” for temperatures above 20 degrees 
# and “Cold” for temperatures 20 degrees or below.

temperatures = [15, 22, 19, 30, 10, 25, 20]

for temp in temperatures:
    if temp > 20:
        print(f"{temp}°C is Warm")
    else:
        print(f"{temp}°C is Cold")


# Task 6: Write a for loop using range() 
# to print the even numbers from 2 to 10.

print("Even numbers from 2 to 10:")
for i in range(2, 11, 2):  # Start at 2, go to 10, step by 2
    print(i, end=' ')
print()


# Task 7: Write a Python program that prints 
# the first 10 multiples of 3 using a
#  for loop and the range() function.

print("First 10 multiples of 3:")
for i in range(1, 11):
    print(3 * i, end=' ')
print()
