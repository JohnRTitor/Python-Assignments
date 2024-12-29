nested_list = []
n = int(input("Enter the number of pairs: "))
for i in range(n):
    pair = list(map(int, input("Enter a pair: ").split()))
    nested_list.append(pair)

print("Even pairs: ")
for pair in nested_list:
    if pair[0] % 2 == 0 and pair[1] % 2 == 0:
        print(pair)
