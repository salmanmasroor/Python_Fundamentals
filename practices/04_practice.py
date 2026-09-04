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
#def missing_number(num_list):

# Count Character Frequency

def count_frequency_char(character):
    char_dict = {"p",2}
    for i in range(0,len(character)):
        print(char_dict.keys())
        """
        if i in char_list[0].keys():
            print("--")
            continue
        """
        print(character[i])
        for j in range(i+1,len(character)):
            print(character[j])


if __name__ == "__main__":
    print(student_mark_analyzer("Ali",[78, 85, 92, 66, 88]))    
    count_frequency_char("programming")