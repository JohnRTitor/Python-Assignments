sentence = input("Enter a sentence: ")
word_to_find = input("Which word to find frequency of? ")

word_count = 0
for word in sentence.split():
    if word.lower() == word_to_find.lower():
        word_count += 1

print(f"The word '{word_to_find}' appears {word_count} times in the sentence.")
