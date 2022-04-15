#Question_1

def hello_name(user_name):
 """Display a simple greeting."""
 print("hello " + user_name.upper() + "!")

hello_name('_username')



#Question_2

def first_odds(n):
    return [x for x in range(0, n+1) if x%2 != 0]

print(first_odds(100))


#Question_3

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list: 
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 100, 34, 68]))


#Question _4


def is_leap_year(a_year):
    
    leap = False
    if (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0:
        leap = True
    return leap
print(is_leap_year(1989))


#Question_5


def is_consecutive(a_list):
     return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

lst = [2, 3, 1, 4, 5] 
print(is_consecutive(lst))