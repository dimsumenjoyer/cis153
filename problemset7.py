'''
Victor Van
00319912
CIS153: Problem Set 7
11/10/2023, Due: 11/14/2023
Note: fuck regular expressions
'''

import re

# Chapter 11, Problem 1:

def regular_expressions_fucking_suck():
    regular_expression_user_input = input("Enter a fucking regular expression: ") #r'\b^([\w.-]+)\b'
    try:
        fucking_compiling_user_input = re.compile(regular_expression_user_input)
    except:
        print("Error.")
    fucking_matches = 0
    with open("access_log.txt", "r") as file:
        for line in file:
            fucking_find_user_input = fucking_compiling_user_input.search(line)
            if fucking_compiling_user_input and fucking_find_user_input is not None:
                fucking_matches += 1
        print(f"There are {fucking_matches} fucking matches for the fucking regular expression: {regular_expression_user_input}.")
    return

#regular_expressions_fucking_suck()

# Chapter 11, Problem 2:

def average():
    file = open("access_log.txt", "r")
    fuck_regular_expressions = r'\d+$'
    find_numbers = re.compile(fuck_regular_expressions)
    number_in_list = 0
    total = 0
    iterations = 0
    average = 0
    for line in file:
        fuck_my_life = find_numbers.findall(line)
        iterations += 1
        if fuck_my_life is not None and fuck_my_life:
            number_in_list = int(fuck_my_life[0])
            total += number_in_list
            average = (total/iterations)
    print(f"Fucking Average: {average}.")
    return

#average()