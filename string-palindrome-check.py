# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Initialize an empty string to store the reversed string
reversed_string = ""
# Iterate through each character in the input string
for ch in input_string:
    # Prepend the character to the reversed string
    reversed_string = ch + reversed_string

# Check if the input string is equal to the reversed string (case insensitive)
if input_string.lower() == reversed_string.lower():
    # If they are equal, the string is a palindrome
    print(input_string, "is a palindrome.")
else:
    # If they are not equal, the string is not a palindrome
    print(input_string, "is not a palindrome.")
