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


# Reverse Words

def reverse_word_v1(word):
    word = list(word.split())
    return word[::-1]

def reverse_word_v2(word):
    word = list(word.split())
    start = 0
    end = len(word)-1
    while start < end:
        temp = word[start]
        word[start] = word[end]
        word[end] = temp
        start += 1
        end -= 1

    return word

def reverse_word_v3(word):
    word_list = []
    temp = ""
    for i in word:
        if i == " ":
            word_list.append(temp)
            temp = ""
        else:
            temp += i

    word_list.append(temp)
    #reverse
    start = 0
    end = len(word_list)-1
    while start < end:
        temp = word_list[start]
        word_list[start] = word_list[end]
        word_list[end] = temp
        start += 1
        end -= 1

    return word_list
    


    return word
if __name__ == "__main__":
    print(grade_system(80))
    print(most_frequent_value([10, 20,20, 10, 30, 20, 10, 40,20,0,1,20]))
    print(reverse_word_v1("Python is very easy"))
    print(reverse_word_v2("Python is very easy"))
    print(reverse_word_v3("Python is very easy"))
