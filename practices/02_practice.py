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

#Prime Number
def is_prime_number(num):
    count = 0
    for i in range(2,num):
        if num % i == 0:
            count += 1
            break

    if count > 0:
        return False
    else:
        return True

#print prime number in range
def prime_no_in_range(num):
    list_prime = [1]
    
    for i in range(2,num+1):
        count = 0
        for j in range(2,num+1):
            if j >= i:
                if count == 0:
                    list_prime.append(i)
                break
            elif j < i:
                if i % j == 0:
                    count += 1
    return list_prime
                
def gcd_between_two(num_one,num_two):
    if num_one > num_two:
        max_length = num_one
    else:
        max_length = num_two

    greater_divisible = 0

    for i in range(2,max_length):
        if num_one % i == 0 and num_two % i == 0:
            greater_divisible = i

    return greater_divisible



if __name__ == "__main__":
    print(reverse_digit_v2(211123123))
    print(is_palidrome_v2(1221))
    print(is_prime_number(1))
    print(prime_no_in_range(20))
    print(gcd_between_two(68,28))