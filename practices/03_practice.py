#print all elements
def print_list(list):
    for i in list:
        print(i)

#Find Sum
def find_sum(list):
    sum = 0  
    for i in list:
        sum += i
    return sum

# Find largest
def largest_number(list):
    return max(list)

def largest_number_v2(list):
    max = list[0]
    for i in list:
        if max < i:
            max = i
    return max

def minimum_number_v2(list):
    min = list[0]
    for i in list:
        if min > i:
            min = i
    return min

def minimum_number(list):
    return min(list)

# Count Even Numbers
def count_even_list(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count +=1
    return count

#Count Positive and Negative
def give_pos_neg(list):
    positive = 0
    negative = 0
    for i in list:
        if i < 0 :
            negative += 1
        elif i > 0 :
            positive +=1
        else:
            pass
    return positive, negative

#Reverse a List
def reverse_list(list):
    return list[::-1]

def reverse_list_v2(list1):
    return list(reversed(list1))

def reverse_list_v3(list_one):
    start = 0
    end = len(list_one)-1
    while start < end:
        temp = list_one[start] 
        list_one[start] = list_one[end]
        list_one[end] = temp
        start +=1
        end -= 1
    return list_one

def search(list_one,value):
    if list_one is not None:
        for i in list_one:
            if i == value:
                return 1

    return -1

def search_v2(list_one,value):
    try:
        result = list_one.index(value)
        if result >= 0:
            return 1
    except:
        return -1

def second_largest(list_one):
    result = sorted(list_one)
    return result[1]

    
if __name__ == "__main__":
    """
    marks = [1,2,3,12,21,32]
    print_list(marks)
    print(find_sum(marks))
    print(largest_number(marks))
    print(largest_number_v2(marks))
    print(minimum_number(marks))
    print(minimum_number_v2(marks))
    print(count_even_list(marks))
    """
    random = [12,3,1,3,-2,1,2,2,0]
    """
    positive,negative = give_pos_neg(random)
    print("positive", positive)
    print("negative", negative)
    print(random)
    print(reverse_list(random))
    print(reverse_list_v2(random))
    print(reverse_list_v3(random))
    """
   
    print(search(random,100))
    print(search_v2(random,111))
    print(second_largest(random))