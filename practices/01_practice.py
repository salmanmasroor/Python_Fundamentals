# Even or Odd
def is_even(num):
    if isinstance(num,int):
        if num % 2 == 0:
            return f"Even: {num}"
        else:
            return f"Odd: {num}"
    else:
        print("Incorrect Value")

result = is_even(24)
print(result)

#Positive, Negative or Zero
def is_positive(num):
    if isinstance(num,int) or isinstance(num,float):
        if num > 0:
            return "Postive"
        elif num < 0:
            return "Negative"
        else:
            return "Zero"

print(is_positive(11))
        
# Largest of 3 Numbers

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
        
leap_year(2024)

