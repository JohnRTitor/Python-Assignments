num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

i = 1
while (i <= num1 and i <= num2):
    if (num1 % i == 0 and num2 % i == 0):
        gcd = i
    i += 1

lcm = (num1 * num2) // gcd

print(f"GCD of {num1} and {num2} is {gcd}")
print(f"LCM of {num1} and {num2} is {lcm}")
