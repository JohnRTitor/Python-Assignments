# Prompt the user to enter the number of elements in the dictionary
size = int(input("How many elements in the dictionary? "))

# Instructions for the user to enter the elements
print("Enter the elements in the dictionary (please enter unique items): ")

# Initialize an empty dictionary to store the original key-value pairs
original_dict = dict()

# Loop to get key-value pairs from the user
for i in range(size):
    # Prompt the user to enter a key and a value
    key, value = input(f"Key Value#{i}: ").split(maxsplit=1)
    # Add the key-value pair to the dictionary
    original_dict[key] = value

# Invert the dictionary (swap keys and values)
inverted_dict = {value: key for key, value in original_dict.items()}

# Display the original dictionary
print("Original dictionary:", original_dict)

# Display the inverted dictionary
print("Inverted dictionary:", inverted_dict)
