word_list = list(input("Enter some words: ").split())

initials = []
for i in range(len(word_list)):
    # Extract the first character of each word and put it in the initials list
    initials.append(word_list[i][0])
    # Remove the first character from the word
    word_list[i] = word_list[i][1:]

print("New words:", word_list)
print("Initials:", initials)
