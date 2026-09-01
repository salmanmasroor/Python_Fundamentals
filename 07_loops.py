"""
Definition: A loop allows you to execute the same block of code multiple times.

Python mainly has two loops:
- for
- while
"""

"""
1. For Loop
    Use "for" when you want to repeat something for a known range.
"""
for i in range(1000):
    print(i)

"""
range(stop) => if single pararmeter.
range(start,stop) => then both given when define starting point.
range(start,stop,step) => how many step jumop if we want more than 1.
"""

for i in range(1,10):
    print(i)

for i in range(1,10+1,2):
    print(i)


num = int(input("Enter the number for iteration: "))

if isinstance(num, int):
    for i in range(1,num+1):
        print(i)
else:
    print("incorrect input")

"""
reverse loop
"""

for i in range(10,0,-1):
    print(i)