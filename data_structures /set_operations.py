# Take input from user
set1 = set(map(int, input("Enter elements of Set 1 (space separated): ").split()))
set2 = set(map(int, input("Enter elements of Set 2 (space separated): ").split()))

# Perform operations
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2

# Display results
print("\nUnion:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)