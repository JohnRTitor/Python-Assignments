import sys

# Taking input from the user for the number of rows
rows = int(input("How many rows? "))

if not rows > 0:
    print("No of rows should be positive")
    sys.exit(0)

# Loop to print each row of the triangle
for i in range(rows):
    # Printing spaces before the stars in each row
    for j in range(rows - i - 1):
        print(end="  ")
    # Printing stars in each row
    for j in range(2 * i + 1):
        print("*", end=" ")
    # Moving to the next line after each row
    print()
