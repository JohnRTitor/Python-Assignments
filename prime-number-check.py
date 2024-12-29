import math

# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter num: "))

# Initialize a flag variable to determine if the number is prime
flag = True

# Check if the number is 0 or 1, which are not prime numbers
if num in [0, 1]:
    flag = False

# Iterate through all numbers from 2 to num // 2
for i in range(2, num // 2):
    # If the current number is a divisor of num, set the flag to False and break
    if num % i == 0:
        flag = False
        break

# Check the flag to determine if the number is prime or composite
if flag:
    # If the flag is True, the number is prime
    print(num, "is a prime number.")
else:
    # If the flag is False, the number is composite
    print(num, "is a composite number.")
