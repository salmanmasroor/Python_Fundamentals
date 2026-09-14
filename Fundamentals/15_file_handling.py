from pathlib import Path

file = open("files/information.txt",'r')
content = file.read()
print(content)
file.close()

# read text file
def file_read(file_name):

    path = Path(__file__).parent / 'files' / f"{file_name}"

    file = open(path, 'r')
    content = file.read()
    print(content)
    file.close()

if __name__ == "__main__":
    file_read("information.txt")