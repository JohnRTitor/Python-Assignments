# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Initialize counters for words, vowels, consonants, and spaces
word_count = 1
vowel_count = 0
consonant_count = 0
space_count = 0

# Iterate through each character in the sentence
for char in sentence:
    # If the character is a space, increment the space and word counters
    if char == " ":
        space_count += 1
        word_count += 1
    # If the character is a vowel, increment the vowel counter
    elif char.lower() in ["a", "e", "i", "o", "u"]:
        vowel_count += 1
    # If the character is a consonant, increment the consonant counter
    elif char.isalpha():
        consonant_count += 1

# Print the entered sentence
print("Entered sentence:", sentence)
# Print the number of words in the sentence
print("Number of words:", word_count)
# Print the number of vowels in the sentence
print("Number of vowels:", vowel_count)
# Print the number of consonants in the sentence
print("Number of consonants:", consonant_count)
# Print the number of spaces in the sentence
print("Number of spaces:", space_count)
