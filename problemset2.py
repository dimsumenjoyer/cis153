'''
Victor Van 9/12/2023
Problem Set 3 - Due: 9/25/2023
Exercises 1-3 from Problem Set 2.
'''

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program.

'''
def salary():
    hours = float(input("Enter Hours: ")) # Enter 45 hours.
    rate = float(input("Enter Rate: ")) # Enter 10 hours.
    if hours > 40:
        hours = hours * 1.5
    pay = hours * rate
    print("Pay: " + str(pay))
    
salary()
'''

def salary():
    try:
        hours = float(input("Enter Hours: ")) # Enter 45 hours for Exercise 1. Enter "20" & "forty" for Exercise 2.
        rate = float(input("Enter Rate: ")) # Enter 10 hours for Exercise 1. Enter "nine" for Exercise 2."
        pay = 0
        if hours <= 40:
            pay += hours * rate
        elif hours > 40:
            pay += ((hours - 40) * 1.5) + (40 * rate)
        
        #pay = hours * rate
        print("Pay: " + str(pay))
    except:
        print("Error. Please enter numeric input.")
#salary()

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error messsage. If the score is between 0.0 and 1.0,
# print a grade using the following type:

# Score: >= 0.9, >= 0.8, >= 0.7, >= 0.6, < 0.6
# Grade: A, B, C, D, F

'''
Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F
'''

def grades():
    try:
        grade = float(input("Enter score: "))
        if 0.0 <= grade <= 1.0:
            if grade >= 0.9:
                grades = "A"
            elif grade >= 0.8:
                grades = "B"
            elif grade >= 0.7:
                grades = "C"
            elif grade >= 0.6:
                grades = "D"
            elif grade < 0.6:
                grades = "F"
        print(grades)
    except:
        print("Bad Score")

#grades()

