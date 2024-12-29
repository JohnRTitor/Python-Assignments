sentence = input("Enter a sentence: ")

word_count = 1
vowel_count = 0
consonant_count = 0
space_count = 0

for char in sentence:
    if char == " ":
        space_count += 1
        word_count += 1
    elif char.lower() in ["a", "e", "i", "o", "u"]:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print("Entered sentence:", sentence)
print("Number of words:", word_count)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Number of spaces:", space_count)
