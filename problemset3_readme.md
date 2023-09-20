Victor Van
Programming for IT (Python)
Professor Michael Penta
Problem Set 3
9/14/2023, Due: 10/2/2023

These are exercises 1-7 problem set 3, chapter 4, from the textbook.

# Exercise 1: Run the problem on your system and see what numbers you get.
The function randint takes the parameters low and high,
and returns an integer between low and high (including both).

I printed random.randint(5, 10) 3 times. I got 6, 5, and 9.
I also tested if random.randint(10, 5) would work because I was curious,
but it doesn't because it reminds to me a traceback error.

# Exercise 2: Move the last name of this function to the top, so the function appears before the definitions.
Run the problem and see what error you get.

This is the code I ran:
repeat_lyrics()
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

# Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of
repeat_lyrics. What happens when you run this program?

This is my code, it is self-explanatory:

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#repeat_lyrics() # When the function is called after it is properly defined, it runs properly.

# Exercise 4: What is the purpose of the "def" keyword in Python

The keyword, "def", both indicates the start of a function and indicates the indented code to be stored for later.

# Exercise 5: What will the following Python program print out?:

I tested this code, and it prints out "ABC Zap ABC" as a result.

def fred():
    print("Zap")

def jane():
    print("ABC")

'''
jane()
fred()
jane()
d) ABC Zap ABC

# Exercise 6: Rewrite your computation with time-and-a-half for overtime and create a function called computepay
which takes two parameters and returns a grade as a string.

I copied and pasted the following code from exercise 2 of problem set 2:

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
salary()

I already made my algorithm a function, but I called it "salary." Therefore, as instructed, I changed my function to
"computepay". I also commented out the hours and rate varibles, because they became redunant since they are now parameters
in my function. Finally, I deleted my try and except conditional statement because I was having issues with calling varibles
before they were technically being defined. I didn't know how to fix it, so I just got rid of "try & except", and added an else
statement to account for non-numeric values. However, my else statement didn't work as expected. Here is my edited code:

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

computepay(40,10)
computepay(45, 10)
computepay("yes", "yes")

# Exercise 7: Rewrite the grade program form the previous chapter using a function called "computegrade"
that takes a score as its parameter and returns a grade as a function.

Score: >= 0.9, >= 0.8, >= 0.7, >= 0.6, < 0.6
Grade: A, B, C, D, F

My previous grade problem was from problem set 2, but I already made it a function. Here was my code:

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

grades()

As instructed, I changed my function name to "computegrade" and added a parameter called "score".
Therefore, I commented out my "score" variable since it is now redunant. I had issues with calling the
variable "grade" when I left it inside the try & except conditional because every parameter I set ended up printing "Bad Score".
Therefore, I had to comment out print("Bad Score") at the except statement and added "grade" as being "Being Score" as default,
before being changed to their respective parameters.

I still have a lot of issues with this code, but it somehow works. My try & except conditional is currently useless,
as if an exception happens I just have it pass and my function would do nothing besides referred to the default "Bad Score".
I think that I could improve this code with the help of a tutor or a professor,
so I'll keep the try & except conditional as an outline.
Here's my code for this algorithm so far:

def computegrade(score):
    grade = "Bad Score"
    try:
        #score = float(input("Enter score: "))
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
        #print(grade)
    except:
        pass #print("Bad Score")
    return print(grade)

computegrade(.9) # outputs "A"
computegrade("Good Score") # It's actually "Bad Score"!

Professor Walton recommended me to try the Cursor text editor yesterday. It comes with a built-in ChatGPT feature.
Sometimes I use ChatGPT to help me debug and find out what's wrong with my code.
However, my goal is to push myself and I don't want to rely too much on AI to write my programs.
While writing this report, I asked ChatGPT 3.5 (via Cursor) how I could improve my code. Here's its response:

Your code looks good overall. However, there are a few suggestions for improvement:

1. Remove the commented-out code: It's a good practice to remove any commented-out code that is no longer needed.
This will make your code cleaner and easier to read.

2. Remove the unnecessary try-except block: Since you are not handling the exception and just passing it,
it is not necessary to have the try-except block in your code.
You can remove it to simplify your code.

3. Use meaningful variable names: Instead of using generic variable names like "grade" and "score",
consider using more descriptive names that convey the purpose of the variable.
This will make your code more readable and easier to understand.

Here's an updated version of your code with these improvements:

def computegrade(score):
    grade = "Bad Score"
    if isinstance(score, float) and 0.0 <= score <= 1.0:
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"
    return grade

print(computegrade(0.9))  # outputs "A"
print(computegrade("Good Score"))  # outputs "Bad Score"

I didn't know that the isinstance function existed,
and I probably would've been able to use it effectively in my code on my own so I didn't edit anything.
