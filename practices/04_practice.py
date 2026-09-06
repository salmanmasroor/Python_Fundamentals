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

def two_sum(num_list,target):
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[i] + num_list[j] == target:
                return (num_list[i],num_list[j])

#remove duplicates
def remove_duplicate_v1(num_list):
    return list(set(num_list))

def remove_duplicate_v2(num_list):
    temp = []
    for i in num_list:
        if i not in temp:
            temp.append(i)
    return temp

#word frequency
def word_frequency(word):
    word_frequency = {}
    word_list = word.split()
    for i in word_list:
        count = 0
        if i in word_frequency:
            continue
        for j in word_list:
            if i == j:
                count += 1
        word_frequency[i] = count
    return word_frequency

def word_frequency_v2(word):
    temp = ""
    word_list = []
    frequency = {}
    for i in word:
        if i == " ":
            word_list.append(temp)
            temp = ""
            continue
        temp += i 
    word_list.append(temp)
    for i in word_list:
        count = 0
        if i in frequency:
            continue
        for j in word_list:
            if i == j:
                count += 1

        frequency[i] = count
    return frequency

# find second largest
def second_largest(num_list):
    max = num_list[0]
    for i in num_list:
        if max < i:
            max = i
    temp = max
    for i in num_list:
        if max == i:
            continue
        if temp < max + i:
            temp = max + i
    temp = temp - max
    return temp

def check_anagram(first_word,second_word):
    string = ""
    if len(first_word) == len(second_word):
        for i in first_word:
            if i in string:
                continue
            for j in second_word:
                if i.lower() == j.lower():
                    string += i.lower()
                
        if len(string) == len(first_word):
            print("Anagram")
        else:
            print("Not Anagram")         
    else:
        return "Not Anagram"

     

if __name__ == "__main__":
    print(student_mark_analyzer("Ali",[78, 85, 92, 66, 88]))    
    print(count_frequency_char_v2("programming"))
    print(missing_number([2,4,7,15,10,23])) # without zero logic
    print(two_sum([2,3,1,2],4))
    print(remove_duplicate_v2([122,1,2,2,3,122,3,22,12,3,4,4]))
    print(word_frequency_v2("python is easy and python is powerful"))
    print(second_largest([14,12,23,12,23,11,2,17,3,2,20]))
    check_anagram("Listen", "Silent")
    a = [12,10,10]
    a.pop(10)
    print(a)