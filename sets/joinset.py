# EX 1
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)  # Output :  {'c', 'b', 'd', 'f', 'e', 'a'}

# EX 2
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)  # Output : {'c', 'a', 'f', 'e', 'b', 'd'}

# EX 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # Oupput : {'apple'}

# EX 4
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print(set1) # Oupput : {'banana', 'google', 'microsoft', 'cherry'}