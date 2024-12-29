# Prompt the user to enter a list of words
word_list = list(input("Enter some words: ").split())

# Initialize the largest_word variable with the first word in the list
largest_word = word_list[0]

# Iterate through each word in the list
for word in word_list:
    # If the current word is longer than the largest_word, update largest_word
    if len(word) > len(largest_word):
        largest_word = word

# Print the largest word found in the list
print("Largest word:", largest_word)
