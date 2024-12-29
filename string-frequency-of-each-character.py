# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Create an empty dictionary to store the frequency of each character
char_freq = dict()

# Iterate through each character in the input string (converted to lowercase)
for ch in input_string.lower():
    # First occurrence of the character, so add it to the dictionary with frequency 1
    if ch not in char_freq:
        char_freq[ch] = 1
    # If the character is already in the dictionary, increment its frequency
    else:
        char_freq[ch] += 1

# Print the characters present and their frequency
print("Characters present and their frequency:")
for ch, freq in char_freq.items():
    print(f"{ch}: {freq}")
