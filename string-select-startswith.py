input_string = input("Enter a string: ")

selected_words = []
for word in input_string.split():
    if word.tolower().startswith("a"):
        selected_words.append(word)

print("Words starting with 'a':", selected_words)
