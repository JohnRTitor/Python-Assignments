number_list = list(map(int, input("Enter some numbers: ").split()))

unique_numbers = []
duplicates = []

for number in number_list:
    if number in unique_numbers:
        duplicates.append(number)
    else:
        unique_numbers.append(number)

print("Original list:", number_list)
number_list = unique_numbers + duplicates
print("List with duplicates moved to the end:", number_list)
