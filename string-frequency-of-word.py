# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Prompt the user to enter the word to find its frequency
word_to_find = input("Which word to find frequency of? ")

# Initialize a counter for the word frequency
word_count = 0

# Iterate through each word in the sentence
for word in sentence.split():
    # If the current word matches the word_to_find (case insensitive), increment the counter
    if word.lower() == word_to_find.lower():
        word_count += 1

# Print the frequency of the word in the sentence
print(f"The word '{word_to_find}' appears {word_count} times in the sentence.")
