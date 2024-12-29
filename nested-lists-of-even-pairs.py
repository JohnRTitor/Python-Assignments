# Initialize an empty list to store the pairs
nested_list = []
# Prompt the user to enter the number of pairs
n = int(input("Enter the number of pairs: "))
# Iterate through the number of pairs
for i in range(n):
    # Prompt the user to enter a pair of numbers and convert them to integers
    pair = list(map(int, input("Enter a pair: ").split()))
    # Add the pair to the nested list
    nested_list.append(pair)

# Print the even pairs
print("Even pairs: ")
# Iterate through each pair in the nested list
for pair in nested_list:
    # Check if both numbers in the pair are even
    if pair[0] % 2 == 0 and pair[1] % 2 == 0:
        # If both numbers are even, print the pair
        print(pair)
