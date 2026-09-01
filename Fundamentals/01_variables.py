"""
Definition:- A variable in Python is a name that refers to a value stored in memory. 
            You can think of it like a label attached to a box containing some data.
"""

"""  Python is dynamically typed, so you don't need to declare the type. """
import keyword
import copy

value = 12
print(value)

# Checking the type of a variable
print(type((value)))

#Rules of Naming Varibale
name = "XYZ"
name1 = "XYZ"
full_name = "XYZ"

print(name, name1, full_name)

# In python prefer snake case for defining the variable 
student_name = "XYZ"
print(student_name)

# keywords can't be variable name
print(keyword.kwlist)

# Mulitple variable assiging in one line
first_name, last_name, full_name = "Hamza", "Jamal", "Hamza Jamal"
print(first_name,last_name,full_name)

# Assign same value to multiple variable in one line 
a = b = c = 2
print(a, b, c)

# varible swapping in python
a = 10 
b = 12

a, b = b ,a 
print(a, b)


# Variable and Memory 
x = 12
y = x                       #Now x and y both point one same box which contain 12 , does not create another memeoy
print(x,y)
print(id(x))
print(id(y))    


x = 11
print(y)                       # now another memory cell create which contain 11 and x pointin it.so x and y has differnt memory.

#if mutable data type then

list_one = [12]
list_two = list_one

list_one.append(40)
print(list_one)
print(list_two)             # the change is reflect in both because both pointing the same memory cell

#to avoid this same memory we use deep copy 

list1 = [122,23]
list2 = copy.deepcopy(list1)
print(id(list1))
print(id(list2))         #now both have different memory cell

list1.append(12)
print(list2)            # change in list1 does not reflect in list2



list_one =  [11]
print(list_two)        # beacuse it is reassignment so they become seperate, that's why diffrent result 



""" CONSTANT in Python 
    Python doesn't have a special const keyword for ordinary variables.
    Instead, programmers use uppercase names to indicate that a value should not be changed.
"""
PI = 3.14
MAX_VALUE = 100

print(PI)
print(MAX_VALUE)
"""
but the uppercase naming convention tells other programmers:
    "This value is intended to remain constant."
"""

"""
1. What is Variable in Python?
2. How to Check data type of vaiable 
3. Keyword can't be varible
4. Rules of Naming Varibale
5. Varibale Name Casing
6. Mulitple variable assiging in one line
7. varible swapping in python
8. Variable and Memory (shallow vs Deep Copy)
9. Constant in Python
"""












