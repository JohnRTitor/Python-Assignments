word_list = list(input("Enter some words: ").split())

largest_word = word_list[0]
for word in word_list:
    if len(word) > len(largest_word):
        largest_word = word

print("Largest word:", largest_word)
