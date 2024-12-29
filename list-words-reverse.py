# Prompt the user to enter a sentence and split it into a list of words
word_list = list(input("Enter a sentence: ").split())

# Reverse the list of words, but do not reverse the words themselves
reversed_word_list = word_list[::-1]

# Iterate through the reversed list and reverse each word
for i in range(len(reversed_word_list)):
    # And store it back in the list
    reversed_word_list[i] = reversed_word_list[i][::-1]

# Print the original list of words
print("Original word list: ", word_list)

# Print the reversed list of words with each word also reversed
print("Reversed word list: ", reversed_word_list)
