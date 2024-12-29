# Prompt the user to enter the first list of numbers and convert them to integers
list1 = list(map(int, input("Enter list1: ").split()))

# Prompt the user to enter the second list of numbers and convert them to integers
list2 = list(map(int, input("Enter list2: ").split()))

# Initialize two empty lists: one for the union and one for the intersection
union_list = []
intersection_list = []

# Iterate through each number in the first list
for x in list1:
    # If the number is also in the second list, it is a common element
    if x in list2:
        intersection_list.append(x)
    # If the number is not in the second list, it is a unique element
    else:
        union_list.append(x)

# Now copy all the elements of the second list to the union_list
# since we have already copied the unique elements of the first list
for x in list2:
    union_list.append(x)

# Print the union of the two lists
print("Union:", union_list)

# Print the intersection of the two lists
print("Intersection:", intersection_list)
