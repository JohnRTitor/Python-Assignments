# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter num: "))

# Initialize the result variable to 1 (since factorial of 0 is 1)
result = 1

# Loop from 1 to the entered number (inclusive)
for i in range(1, num + 1):
    # Multiply the result by the current number in the loop
    result *= i

# Print the factorial of the entered number
print("Factorial of", num, "is", result)
