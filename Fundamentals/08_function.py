"""
Definition: 
A function is a reusable block of code designed to perform a specific task.
"""
def add(a,b): # a and b are parameters
    return a+b

result = add(12,23) # 12 and 23 are arguments
print(result)


# fucntion composition
def calculate(a,b):
    return add(a,b) + 5

result = calculate(10,3)
print(result)

def print_name(name="Guest"): # default arguments
    print(name)

print_name()
print_name(name="Hamza") # Keyword arguments