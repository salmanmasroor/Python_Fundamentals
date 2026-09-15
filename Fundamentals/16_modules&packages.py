"""
What Is a Module?

A module is a Python file containing reusable code such as:

Variables
Functions
Classes
Statements

A module normally has a .py extension.
"""

# Importing a Module
import random_modules 
print(random_modules.sum(12,23))
print(random_modules.sub(40,20))

# Import Specific Functions
from random_modules import sum, sub
print(sum(10,5))
print(sub(20,8))

# Import with Alias : Use as to give a shorter name

import random_modules as module
print(module.sum(20,40))
print(module.sub(24,22))

# Built-in Modules [math, random, datetime, os, json]
# math
import math
print(int(math.sqrt(25)))

#radmon
import random
print(random.randint(1,10))

#datetime 
import datetime as d
print(d.datetime.now())

#os
import os
print(os.getcwd())

"""
What Is a Package?
A package is a folder containing multiple related Python modules.

project/
│
├── main.py
│
└── tools/
    ├── __init__.py
    ├── calculator.py
    └── converter.py

Here:

calculator.py → module
converter.py → module
tools/ → package

Module vs Package

Module	                Package

Usually one .py file	Folder containing modules
Stores reusable code	Organizes related modules
Example: calculator.py	Example: tools/
"""

from tools import calculator
print(calculator.mul(12,23))

# or

from tools.calculator import mul
print(mul(11,5))


# __name__ == "__main__" 
"""
Code inside this block runs when the file is executed directly.
It does not run when the file is imported as a module.
"""


"""

“Why does a __pycache__ folder appear after I import/use a module?”:

Python/CPython creates a .pyc file inside __pycache__.
CPython converts your .py code into bytecode and saves that bytecode as a .pyc file.
Next time you import the module, Python can use the cached bytecode instead of doing all the compilation work again.
"""
if __name__ == "__main__":
    print(mul(11,5))
    