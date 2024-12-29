# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter num: "))

# Initialize a variable to store the sum of the divisors
sum = 0

# Iterate through all numbers from 1 to num-1
for i in range(1, num):
    # If the current number is a divisor of num, add it to the sum
    if num % i == 0:
        sum += i

# Check if the sum of the divisors is equal to the original number
if sum == num:
    # If they are equal, the number is a perfect number
    print(num, "is a perfect number.")
else:
    # If they are not equal, the number is not a perfect number
    print(num, "is not a perfect number.")
