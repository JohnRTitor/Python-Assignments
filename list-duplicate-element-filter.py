# Prompt the user to enter a list of numbers and convert them to integers
number_list = list(map(int, input("Enter some numbers: ").split()))

# Initialize two empty lists: one for unique numbers and one for duplicates
unique_numbers = []
duplicates = []

# Iterate through each number in the input list
for number in number_list:
    # If the number is already in the unique_numbers list, it is a duplicate
    if number in unique_numbers:
        duplicates.append(number)
    # If the number is not in the unique_numbers list, add it to unique_numbers
    else:
        unique_numbers.append(number)

# Print the original list of numbers
print("Original list:", number_list)

# Combine the unique numbers and duplicates, with duplicates moved to the end
number_list = unique_numbers + duplicates

# Print the modified list with duplicates moved to the end
print("List with duplicates moved to the end:", number_list)
