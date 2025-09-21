list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Find the intersection of the two sets
common_elements_set = set1.intersection(set2)

# If you need the result as a list, convert it back
common_elements_list = list(common_elements_set)

print(f"Common elements (as a set): {common_elements_set}")
print(f"Common elements (as a list): {common_elements_list}")
