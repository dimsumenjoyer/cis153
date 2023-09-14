Victor Van
Programming for IT (Python)
Professor Michael Penta
Problem Set 2
9/12/2023, Due: 9/25/2023

For problem set 3, I worked on exercises 1-3.

# Exercise 1 & 2:

Exercise 1 from chapter 3 of the textbook, "Python for Everbody: Exploring Data for Python 3"
instructed me to rewrite my pay computation for employees working over 40 hours to 1.5 times their salary.

Therefore, I copied and pasted my code from exercise 3 from problem set 1.
I added an if statement so that if hours > 40, then the original hours is multiplied by 1.5 to get the overtime hours.

Exercise 2 from chapter 3 of the textbook instructed me to rewrite the salary program to use a try & except conditional
statement to account for non-numeric inputs that would exit the program.

Therefore, I just added "try:" with an indentation before my other code and added "except: "
that prints "Error. Please enter numeric input." to account for non-numerical values. 
I didn't realize this beforehand but when "except" is utilized, it automatically exists the program.

# Exercise 3: 

Exercise 3 instructs me to write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error messsage. If the score is between 0.0 and 1.0, it
print a grade accordingly. If the score is out of range or a non-numerical value,
it outputs "Bad Score". Again, I used a function to create this algorithm. It also has 8 chained conditionals.
Initially, this code didn't work as intended. But Professor Penta pointed out that I forgot a simple print function
to print out the corresponding grades.