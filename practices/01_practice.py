# Even or Odd
def is_even(num):
    if isinstance(num,int):
        if num % 2 == 0:
            return f"Even: {num}"
        else:
            return f"Odd: {num}"
    else:
        print("Incorrect Value")



#Positive, Negative or Zero
def is_positive(num):
    if isinstance(num,int) or isinstance(num,float):
        if num > 0:
            return "Postive"
        elif num < 0:
            return "Negative"
        else:
            return "Zero"


        
# Largest of 3 Numbers
def largest_number():
    num_one = int(input("Enter the First Number: "))
    num_two = int(input("Enter the Second Number: "))
    num_third = int(input("Enter the Third Number: "))

    if num_one > num_two and num_one > num_third:
        print(num_one," is the largest value.")
    elif num_two > num_one and num_two > num_third:
        print(num_two, " is the largest value.")
    elif num_third > num_one and num_third > num_two:
        print(num_third," is the largest value.")
    else:
        pass


# Grade Calculator
def grade_calculator():
    marks = int(input("Enter the marks: "))

    if marks >= 90:
        print("Grade A")
    elif marks >= 85:
        print("Grade A-")
    elif marks >= 80:
        print("B")
    elif marks >= 75:
        print("B-")
    elif marks >= 70:
        print("C")
    elif marks >= 65:
        print("C-")
    elif marks >= 60:
        print("D")
    elif marks >= 50:
        print("E")
    else:
        print("F")


#Leap Year

def leap_year(year):
    if isinstance(year,int):
        if year % 4 == 0:
            print("leap_year")
        else:
            print("Not Leap Year")

    else:
        print("Year correctly")




# Multiplication

def table(num):
    if isinstance(num,int):
        for i in range(1,11):
            print(num," * ",i," = ",num*i)



# sum of digit

def sum_of_digit(num):
    if isinstance(num,int):
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum



# factorial
def factorial(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i
    return sum

# count digits

def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1

    return count

# Sum of 1 to N       
def sum_of_n(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum



if __name__ == "__main__":
    """
    result = sum_of_nth(881188) 
    print(result)
    table(12)
    leap_year(2024)
    print(is_positive(11))
    result = is_even(24)
    print(result)
    fact = factorial(5)
    print(fact)
    """
    print(count_digits(12433242343))

    print(sum_of_n(10))
   
