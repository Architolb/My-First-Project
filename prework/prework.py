#Question_1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
 """Display a simple greeting."""
 print("hello " + user_name.upper() + "!")

hello_name('_username')



#Question_2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds()
def first_odds(n):
    return [x for x in range(0, n+1) if x%2 != 0]

print(first_odds(100))


#Question_3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list: 
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 100, 34, 68]))


#Question _4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    
    leap = False
    if (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0:
        leap = True
    return leap
print(is_leap_year(1989))


#Question_5
#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
     return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

lst = [2, 3, 1, 4, 5] 
print(is_consecutive(lst))