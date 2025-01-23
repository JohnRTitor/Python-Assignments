rows = int(input("How many rows? "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(end="  ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(end="  ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
