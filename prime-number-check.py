import sys
import math

num = int(input("Enter num: "))

flag = True

if num in [0, 1]:
    flag = False

for i in range(2, num // 2):
    if num % i == 0:
        flag = False
        break

if flag:
    print(num, "is a prime number.")
else:
    print(num, "is a composite number.")
