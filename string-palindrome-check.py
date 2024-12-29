input_string = input("Enter a string: ")

reversed_string = ""
for ch in input_string:
    reversed_string = ch + reversed_string

# Check if the input string is equal to the reversed string (case insensitive)
if input_string.lower() == reversed_string.lower():
    # If they are equal, the string is a palindrome
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")
