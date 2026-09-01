"""
Definition: A condition allows your program to make a decision.
"""

age = 18

# if statement 

if age >= 18:
    print("Allowed to Vote")


# else if if condition not match 
age = 12
if age >= 18:
    print("Allowed to Vote")
else:
    print("Not allowed to Vote")


# Use elif when you have multiple possibilities.

marks_obtained = 12

if marks_obtained >= 20:
    print("Excellent")
elif marks_obtained >= 15:
    print("Good")
elif marks_obtained >= 10:
    print("well")
else:
    print("need to improve")