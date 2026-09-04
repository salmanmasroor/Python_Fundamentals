"""
Definition:
-Dictionaries are used to store data values in key:value pairs.
-A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
-As of Python version 3.7, dictionaries are ordered. 
-In Python 3.6 and earlier, dictionaries are unordered.
"""
#Creating a Dictionary
student = {
    "name" : "Usman",
    "age" : 22,
    "marks" : [12,23,34,12,25,30]
}
print(student)

# key must be unqiue if not then it will replace will latest one 
student_one = {
    "name" : "Shahid",
    "name" : "Jamal"
}
print(student_one)

# accessing values
print(student["name"])
print(student["age"])

# Adding a New Key-Value Pair
student["city"] = "Lhr"
print(student)

#Update a value 
student['city'] = "Sialkot"
print(student)

# Removing a Element
del student["city"]
print(student)

student.pop("age")
print(student)

# Check if Key Exists
print('name' in student)
print('age' in student)

#Dictionary Length
print(len(student))

#Loop Through a Dictionary
for key in student:
    print(key)

for key in student:
    print(student[key])

for values in student.values():
    print(values)

for key,values in student.items():
    print(key, values)

#keys() values() items()

print(student.keys())
print(student.values())
print(student.items())

# get()
# instead this 
print(student["name"])

# we can use get too 
print(student.get("name"))
#(If the key doesn't exist, get() returns None instead of immediately raising a KeyError)

# Nested Dictionary
students = {
    "student1": {
        "name": "Ali",
        "age": 20
    },
    "student2": {
        "name": "Ahmed",
        "age": 22
    }
}
print(students)
print(students["student1"]["name"])

for key in students:
    print(students[key]["name"])

# Dictionary with List
print(student['marks'][0])

for i in student:
    if i == 'marks':
        for j in student['marks']:
            print(j)