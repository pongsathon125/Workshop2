#EX 1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#Output : {'banana', 'cherry', 'orange', 'apple'}


#EX 2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
#Output : {'banana', 'cherry', 'mango', 'papaya', 'pineapple', 'apple'}