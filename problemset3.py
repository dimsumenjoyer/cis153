'''
Victor Van
Programming for IT (Python)
Professor Michael Penta
Problem Set 3 Exercises 1-7
9/13/2023, Due: 10/2/2023
'''

# Exercise 1:

import random

#x = random.randint(1, 10)
#print(x) # I got 1, 10, and 6.

# Exercise 2 & 3:

#repeat_lyrics()
'''
NameError: name 'repeated_lyrics' is not defined
The error occurs because you must define functions & varibles before they're called.
Python runs code sequentially from up to down, in the order that functions are called.
'''

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#repeat_lyrics() # When the function is called after it is properly defined, it runs properly.

# Exercise 4: What is the purpose of the "def" keyword in Python

'''
d) b and c are both true.
-> b) It indicates the start of a function.
-> c) It indicates that the following indented section of code is to be stored for later.
'''

# Exercise 5: What will the following Python program print out?

def fred():
    print("Zap")

def jane():
    print("ABC")
    
'''
jane()
fred()
jane()
# d) ABC Zap ABC
'''

# Exercise 6:

def computepay(hours, rate):
    try:
        pay = 0
        if hours <= 40:
            pay += hours * rate
            print("Pay: " + str(pay))
        elif hours > 40:
            pay += ((hours - 40) * 1.5) + (40 * rate)
            pay += hours * rate
            print("Pay: " + str(pay))
    except:
        print("Error. Please enter numeric input.")

#computepay(40,10)
#computepay(45, 10)
#computepay("yes", "yes")

# Exercise 7:

def computegrade(score):
    grade = "Bad Score"
    try:
        if 0.0 <= score <= 1.0:
            if score >= 0.9:
                grade = "A"
            elif score >= 0.8:
                grade = "B"
            elif score >= 0.7:
                grade = "C"
            elif score >= 0.6:
                grade = "D"
            elif score < 0.6:
                grade = "F"
    except:
        pass #print("Bad Score")
    return print(grade)

#computegrade(.9) # outputs "A"
#computegrade("Good Score") # It's actually "Bad Score"!
