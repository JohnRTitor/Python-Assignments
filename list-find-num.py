num_list = list(map(int, input("Enter the list: ").split()))

x = int(input("Which element to search for? "))

if x in num_list:
    print(x, "is present in the list")
else:
    print(x, "is not present in the list")
