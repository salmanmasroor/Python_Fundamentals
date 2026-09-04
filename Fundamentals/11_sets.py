"""
Definition:
Set is a built-in Python data type used to store a collection of unique items.

Stores only unique elements; duplicate values are automatically removed.
Unordered collection, so elements do not have a fixed position and cannot be accessed using indexes.
Supports fast search, insertion and deletion operations using hashing internally.
"""

# creating  sets
numbers = {1,3,4,5,7}
print(numbers)
print(type(numbers))

# filter out duplicate automatically 
num = {10,1,2,12,10,2,20}
print(num)
print(sorted(num))

# empty sets
x = set() # this correct

# it takes as dictionary
x = {} # if you want to create set then it not correct because it takes as dictonary 

# adding element
num.add(22)
print(num)

# remove element 
num.remove(20) # if element not exist then it give error
print(num)

num.discard(12) # if element not exist it does nothing
print(num)

# membership
print(1 in num)

# Loop through set
for i in num:
    print(i)

# we can not use (for range) loop beacuse indexing is not allowed in sets

# length
print(len(num))

# SET Operations 
# Union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)

# Intersection
print(a & b)

# Difference
print(a - b)
print(b - a)

# Symmetric Difference (Elements that are in either set, but not both)
print(a ^ b)