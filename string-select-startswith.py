# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Initialize an empty list to store words starting with 'a'
selected_words = []

# Split the input string into words and iterate through each word
for word in input_string.split():
    # Check if the word starts with 'a' (case insensitive)
    if word.lower().startswith("a"):
        # If it does, add the word to the selected_words list
        selected_words.append(word)

# Print the list of words that start with 'a'
print("Words starting with 'a':", selected_words)
