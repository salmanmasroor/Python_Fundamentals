"""
Definition:
A tuple is an immutable ordered collection of elements.

Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
Can hold elements of different data types.
These are ordered, heterogeneous and immutable.

"""

# Creating tuple
values = (12,10,11)
print(values)

# Single-element tuple needs a comma
values = (10,)
print(type(values))

# Without the comma, it's just an integer
values = (10)
print(type(values))

# Indexing
data = (12,23,12,23)
print(data[0])

# Slicing
print(data[0:3])

# Loop Through Tuple
for i in range(len(data)):
    print(data[i])

for i in data:
    print(i)

# check isf value exist
print(12 in data)

# Length
print(len(data))

# Tuple is immutable
# data[3] = 12 give error 

# count
print(data.count(12))

# index
print(data.index(12))

# tuple unpacking
first,*second = data
print(first)
print(second)

# packing
students = "Ali", 20 
print(students)

# nested tuple
students = ((2,1,2),(33,12))
print(students[0][0])
for i in students:
    for j in i:
        print(j)

"""
| Tuple                         | List                      |
| ----------------------------- | ------------------------- |
| `(10, 20, 30)`                | `[10, 20, 30]`            |
| Immutable                     | Mutable                   |
| Cannot change elements        | Can change elements       |
| Generally used for fixed data | Used for changeable data  |
| `count()`, `index()`          | Many modification methods |

"""