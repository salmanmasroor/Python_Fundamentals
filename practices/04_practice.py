#Find the First Duplicate
number_list = [10, 20, 30, 20, 40, 10]

for i in range(0,len(number_list)-1):
    for j in range(i+1,len(number_list)):
        if number_list[i] == number_list[j]:
            found = True
            break
    if found:
        print(number_list[i])
        break    

#Student Mark Analyzer
def student_mark_analyzer(name,marks_list):
    max_marks = max(marks_list)
    min_marks = min(marks_list)
    avg_marks = lambda x: sum(x) / len(marks_list)

    return {
        "name" : name,
        "Highest" : max_marks,
        "Lowest" : min_marks,
        "Average" : avg_marks(marks_list)
    } 

#Find Missing Number
def missing_number(num_list): # without zero
    temp = 0
    missing_list = []
    num_list = sorted(num_list)
    for i in num_list:
        if i - temp == 1:
            temp = i
        else:    
            for row in range(temp+1,i):
                print(row)
                missing_list.append(row)
            temp = i
    return missing_list




# Count Character Frequency
def count_frequency_char_v1(character):
    char_dict = {}

    for i in range(len(character)):
        count = 1

        if character[i] in char_dict:
            continue

        for j in range(i+1,len(character)):
            if character[i] == character[j]:
                count += 1

        char_dict[character[i]] = count

    return char_dict

def count_frequency_char_v2(character):
    char_dict = {}

    for i in character:
        count = 0
        if i in char_dict:
            continue
        for j in character:
            if i == j:
                count += 1
        char_dict[i] = count

    return char_dict
            


if __name__ == "__main__":
    print(student_mark_analyzer("Ali",[78, 85, 92, 66, 88]))    
    print(count_frequency_char_v2("programming"))
    print(missing_number([2,4,7,15,10,23])) # without zero logic