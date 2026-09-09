# Student Grade Systen

def grade_system(num):
    grade = None
    if num >= 90:
        grade = 'A+'
    elif num >= 80:
        grade = 'A-'
    elif num >= 70:
        grade = 'B'
    elif num >= 60:
        grade = 'C'
    elif num >= 50:
        grade = 'E'
    else:
        grade ='F'
    
    return grade

# FIND THE MOST frequent Value
def most_frequent_value(num_list):
    max = 0
    value = None
    for i in range(len(num_list)):
        count = 0
        for j in range(len(num_list)):
            if num_list[i] == num_list[j]:
                count += 1
        if max < count:
            max = count
            value = num_list[i]

    return (value, max)


if __name__ == "__main__":
    print(grade_system(80))
    print(most_frequent_value([10, 20,20, 10, 30, 20, 10, 40,20,0,1,20]))