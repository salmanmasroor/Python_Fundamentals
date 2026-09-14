"""
Definition: File handling in Python is used to perform operations such as reading, writing, and modifying data stored in files.

File Modes

| Mode  | Meaning                                 |
| ----- | --------------------------------------- |
| `"r"` | Read file                               |
| `"w"` | Write file; overwrites existing content |
| `"a"` | Append content at the end               |
| `"x"` | Create new file; error if exists        |
| `"b"` | Binary mode                             |
| `"t"` | Text mode                               |

"""
from pathlib import Path
"""
file = open("files/information.txt",'r')
content = file.read()
print(content)
file.close()
"""

# read text file
def file_read(file_name):

    path = Path(__file__).parent / 'files' / f"{file_name}"

    file = open(path, 'r')
    content = file.read()   # [read] :- Returns one string containing the entire file, [readlines] :- Returns a list of strings, where each line is an item:
    print(content)          # [readline] :- Read one line
    file.close()

# write the data if exist again run it the it override it for that reason use append "a"
def write_file(file_name):

    path = Path(__file__).parent / 'files' / f"{file_name}"
    file = open(path,'w')
    file.write(" asdasd data adssad asdsada")
    file.close()

#append file 
def append_file(file_name):

    path = Path(__file__).parent / 'files' / f"{file_name}"
    file = open(path,'a')
    file.write(" asdasd data adssad asdsada")
    file.close()

# context manager : This is the recommended approach because Python automatically closes the file.
def read_file(file_name):
    path = Path(__file__).parent / 'files' / f"{file_name}"
    with open(path,'r') as file:
        content = file.read()
        print(content)

# read thorugh loop
def read_file_v2(file_name):
    path = Path(__file__).parent / 'files' / f"{file_name}"
    with open(path,'r') as file:
        for line in file:
            print(line.strip()) #strip use to remove whitespaces from start and end.
            print("----")

#check file content exist 
def is_exist(file_name,search):
    path = Path(__file__).parent / 'files' / f"{file_name}"
    with open(path) as file:
        content = file.read()

    if search in content:
        print(True)
    else:
        print(False)

#Handle File Errors
"""
try:
    file_name = "information1.txt"
    path = Path(__file__).parent / 'files' / f"{file_name}"
    with open(path,'r') as file:
        content = file.read()
        print(content)
except FileExistsError as e:
    print(e)
"""

#File Position : tell() shows the current cursor position.
"""
file_name = "information.txt"
path = Path(__file__).parent / 'files' / f"{file_name}"
with open(path, "r") as file:

    print(file.tell())
    print(file.read(2))
    print(file.tell())
"""
#Move Cursor: seek() moves the cursor back to the beginning.
file_name = "information.txt"
path = Path(__file__).parent / 'files' / f"{file_name}"
with open(path, "r") as file:
    print(file.read(11))
    print(file.read(1))
    print(file.seek(0)) # take cursor at start posititon
    print(file.tell())
    print(file.read(1))


if __name__ == "__main__":
    #file_read("information.txt")
    #write_file("data.txt")
    #append_file("data.txt")
    #read_file_v2("information.txt")
    is_exist("information.txt","is")