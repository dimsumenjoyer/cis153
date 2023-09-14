Victor Van
Programming for IT (Python)
Professor Michael Penta
Problem Set 1
9/11/2023, Due: 9/18/2023

I completed exercises 1-5 from chapter 2 from the "Python for Everyone" textbook.

# Exercise 1: Type the following statements in the Python interpreter to see what they do.

5; 5 is an integer, but it needs to be stored into a varible or printed out. 
Just an integer by itself will result in an error.

x = 5; 5 being stored into a varible called x. In class earlier today,
I learned that the float and integers are calculated first, then stored to varibles.
("Right to left.")

x = x + 1; this would might make sense in math because it would be 0 = 1.
However, this takes the varible x prior which is = 5 and adds 1.
The output is 6 because x = x + 1 becomes x = (5) + 1.

# Exercise 2: Write a problem to prompt the user for hours and rate per hour to compute gross pay.

I made functions for all of my code because I usually have them print out stuff.
What the code inside the function does stays the same, 
but to help me be organized I like to comment out parts where my code would otherwise output something.

When the function "name" is prompted, it asks you to "Enter your name: ".
It stores that to a varible, y.
Then, it concatenates that string to another string containing "Hello ".
Finally, when printed out, it outputs "Hello [y = name]".

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

When the function "salary" is prompted, this program asks you to "Enter Hours: ",
and "Enter Rate: ", which are stored as strings. However, I used float() to convert
the strings into floats.

Your salary are your the number of hours you've worked multipled by your hourly salary.
Hence, pay = hours * rate.

# Exercise 4: Assume that we execuse the following assignment statements.

width = 17
height = 12.0

For each of the following expressions, write the value of the expression and the type
(of the value of the expression:

1) width//2
2) width/2.0
3) height/3
4) 1 + 2 * 5

My code is self-explanatory. I named my varibles as the type of operation used (e.g. quotient).
I printed them out as instructed for their answers, 
and commented their answers right next to their respective print statements. The print statements
are then commented out after I've tested it. I've also determined the varible types manually
by printing out type(varible_name). I also commented the varible type, then commented out the print statement.

# Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.

I didn't know the conversation formula for Celsius to Fahrenheit, so I just googled it.

When prompted, the program asks you for the temperature in Celsius. 
It stores your input as a string, so I made to manually convert it into a float.
Then, it takes that float value and plugs it into the formula.
Afterwards, it stores the output of that formula into a varible called "fahrenheit."
Finally, it outputs "The converted temperature is " + str(fahrenheit) + " degrees Fahrenheit.").