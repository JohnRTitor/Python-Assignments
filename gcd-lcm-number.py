import sys

# Taking input from the user for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Check if the numbers are positive
if not num1 > 0 or not num2 > 0:
    print("Please enter positive numbers")
    sys.exit(0)

# Initialize the variable for the loop
i = 1
# Loop to find the greatest common divisor (GCD)
while (i <= num1 and i <= num2):
    if (num1 % i == 0 and num2 % i == 0):
        gcd = i
    i += 1

# Calculate the least common multiple (LCM)
lcm = (num1 * num2) // gcd

# Print the GCD and LCM
print(f"GCD of {num1} and {num2} is {gcd}")
print(f"LCM of {num1} and {num2} is {lcm}")
