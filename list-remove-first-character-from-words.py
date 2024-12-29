# Prompt the user to enter a list of words
word_list = list(input("Enter some words: ").split())

# Initialize an empty list to store the initials of each word
initials = []

# Iterate through each word in the list
for i in range(len(word_list)):
    # Extract the first character of each word and put it in the initials list
    initials.append(word_list[i][0])
    # Remove the first character from the word
    word_list[i] = word_list[i][1:]

# Print the modified list of words with the first character removed
print("New words:", word_list)

# Print the list of initials
print("Initials:", initials)
