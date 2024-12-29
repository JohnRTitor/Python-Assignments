import math
import sys

# Prompt the user to enter the coefficients a, b, and c of the quadratic equation
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Calculate the discriminant using the formula b^2 - 4ac
discriminant = b ** 2 - 4 * a * c

# Check if the discriminant is negative, which means no real roots are available
if discriminant < 0:
    print("No real roots available.")
    sys.exit(0)

# Calculate the two roots using the quadratic formula
root1 = (- b + math.sqrt(discriminant)) / (2 * a)
root2 = (- b - math.sqrt(discriminant)) / (2 * a)

# Check if the discriminant is positive, which means there are two distinct roots
if discriminant > 0:
    print("Roots are:", root1, ",", root2)
else:
    # If the discriminant is zero, there is only one root
    print("Only root is:", root1)
