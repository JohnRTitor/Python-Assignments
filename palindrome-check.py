# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter num: "))

# Store the original number in a temporary variable
temp = num
# Initialize a variable to store the reversed number
reverse = 0

# Loop to reverse the digits of the number
while temp > 0:
    # Extract the last digit of the number
    digit = temp % 10
    # Append the digit to the reversed number
    reverse = reverse * 10 + digit
    # Remove the last digit from the temporary number
    temp //= 10

# Check if the reversed number is equal to the original number
if reverse == num:
    # If they are equal, the number is a palindrome
    print(num, "is a palindrome number")
else:
    # If they are not equal, the number is not a palindrome
    print(num, "is not a palindrome.")
