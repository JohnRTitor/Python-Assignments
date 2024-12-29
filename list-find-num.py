# Prompt the user to enter a list of numbers and convert them to integers
num_list = list(map(int, input("Enter the list: ").split()))

# Prompt the user to enter the number to search for and convert it to an integer
x = int(input("Which element to search for? "))

# Check if the number is present in the list
if x in num_list:
    # If the number is found, print that it is present
    print(x, "is present in the list")
else:
    # If the number is not found, print that it is not present
    print(x, "is not present in the list")
