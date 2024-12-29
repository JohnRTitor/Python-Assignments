# Prompt the user to enter the first number and convert it to an integer
num1 = int(input("Enter num1: "))

# Prompt the user to enter the second number and convert it to an integer
num2 = int(input("Enter num2: "))

# Prompt the user to enter the third number and convert it to an integer
num3 = int(input("Enter num3: "))

# Compare the three numbers to find the largest one
if num1 > num2 and num1 > num3:
    # If num1 is greater than both num2 and num3, it is the largest
    maximum = num1
elif num2 > num3:
    # If num2 is greater than num3, it is the largest
    maximum = num2
else:
    # Otherwise, num3 is the largest
    maximum = num3

# Print the largest number
print(maximum, "is largest")
