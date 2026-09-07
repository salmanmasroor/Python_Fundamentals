"""
Definition:
Exception handling is used to handle errors that happen while a program is running, 
so the program can respond gracefully instead of crashing.
"""


#Why Do We Need Exception Handling?
#without exception handling
num = int(input("Enter the number:"))
print(10/num)

#if input i send zero python code crashes with ZeroDivisionError

#with exception handling

num = int(input("Enter the number: "))
try:
    print(10/num) 
except ZeroDivisionError:
    print("Cannot divided by zero") # Now the program doesn't crash.


# try and except
try:
    # code that might cause error
    print(10/0)
except ZeroDivisionError: 
    # handle the error
    print("cannot divided by zero")

# Catch a Specific Exception

try:
    num_one = int(input("Enter the 1st number: "))
    num_two = int(input("Entert the 2nd number: ")) 
    print(num_one/num_two)

except ValueError:
    print("Please,Enter the number")
except ZeroDivisionError:
    print("Divided by zero")

#Common Exception
"""
| Exception           | Common cause              |
| ------------------- | ------------------------- |
| `ValueError`        | Invalid value conversion  |
| `TypeError`         | Wrong data type operation |
| `ZeroDivisionError` | Division by zero          |
| `IndexError`        | Invalid list/tuple index  |
| `KeyError`          | Missing dictionary key    |
| `NameError`         | Variable doesn't exist    |
| `FileNotFoundError` | File doesn't exist        |
"""

#else: else runs only when no exception occurs.
try:
    num = int(input("Enter the number: "))
except ValueError:
    print("Enter the number only.")
else:
    print(num)


#finally: finally always executes, whether there is an error or not.

try:
    num = int(input("Enter number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally: 
    print("Run")

#Complete Structure
"""
try:
    # risky code

except ValueError:
    # handle ValueError

except ZeroDivisionError:
    # handle ZeroDivisionError

else:
    # runs if no error

finally:
    # always runs
"""
#raise: You can intentionally create an exception using raise.
age = int(input("Enter the age: "))
if age < 0:
    raise ValueError("age can not be negative")

#Exception Object: You can store the error in a variable:
try:
    num = 12
    print(num/0)

except ValueError as error:
    print("error")

except Exception as e: #Exception → catches most standard runtime exceptions [Catches a broad range of exceptions and gives you the exception object.]
    print(e)