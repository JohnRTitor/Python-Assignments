import math
import sys

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("No real roots available.")
    sys.exit(0)

root1 = (- b + math.sqrt(discriminant)) / (2 * a)
root2 = (- b - math.sqrt(discriminant)) / (2 * a)

if discriminant > 0:
    print("Roots are:", root1, ",", root2)
else:
    print("Only root is:", root1)
