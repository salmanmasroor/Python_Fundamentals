# reverse the digit 
from importlib import import_module   #(used beacuse do not want to change file name)

practice = import_module("01_practice")
count_digits = practice.count_digits

def reverse_digit_v1(num):  # without typecasting 
    if isinstance(num,int):
        digit_length = count_digits(num)
        reverse, total = 0, 10 ** (digit_length-1)
        while num > 0:
            reverse += (num % 10)*total
            num = num // 10
            total = total // 10
        return reverse 
    else:
        print("please enter the number correctly")

def reverse_digit_v2(num):
    reverse = ""
    while num > 0:
        reverse += str(num % 10)
        num = num // 10

    return int(reverse)

# palidorme
def is_palidrome_v1(num):
    temp = num
    reverse = ""
    while num > 0:
        reverse += str(num % 10)
        num = num // 10

    reverse = int(reverse)
    if temp == reverse:
        return 1
    else:
        return 0

def is_palidrome_v2(num):
    temp = reverse_digit_v2(num)
    if temp == num:
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(reverse_digit_v2(211123123))
    print(is_palidrome_v2(1221))