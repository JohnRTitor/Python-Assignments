list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

union_list = []
intersection_list = []

for x in list1:
    # Common elements
    if x in list2:
        intersection_list.append(x)
    # Unique elements
    else:
        union_list.append(x)

# Now copy all the elements of list2 to union_list
# since we have already copied the unique elements of list1
for x in list2:
    union_list.append(x)

print("Union:", union_list)
print("Intersection:", intersection_list)
