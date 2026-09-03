"""
List is a built-in data structure used to store an ordered collection of items. 
They are dynamic, resizable and capable of storing multiple data types.

Mutable: list elements can be changed, updated, added, or removed after the list is created.
Ordered: elements maintain the order in which they are inserted.
Index-based: elements are accessed using their position, starting from index 0.

"""

# creating list 
marks = [12,23,11,25]
students = []


# indexing
print(marks[0])
print(marks[2])
print(marks[-1])

#update element 
marks[0] = 10
print(marks)

#traverse a list 
for i in range(len(marks)):
    print(marks[i])

for i in marks:
    print(i)

#membership
result = 10 in marks
print(result)

#slicing
print(marks[0:2])
print(marks[0:len(marks):2])

#add element
marks.append(15)
print(marks)

#remove element
marks.remove(10)
print(marks)

#nested list
data = [[1,2,32,12],[2,23,12,23]]
print(data[0][0])
print("-----------------")

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j])

print("----------------")

for row in data:
    for element in row:
        print(element)


# function and list

def show_marks(marks):
    return marks

student_marks = [12,32,43,2,34,23,12]

print(show_marks(student_marks))




