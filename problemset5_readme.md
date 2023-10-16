'''
Victor Van
Programming for IT (Python)
Professor Michael Penta
Problem Set 5, Chapter 6, 7, etc
9/25/2023, Due: 10/9/2023
'''

# Chapter 6, Exercise 1:

I made a function called print_backwards which takes the length
of the string that a user inputs and subtracts 1 for every
iteration of the while loop. Each iteration prints the length of
the string, while each iteration is 1 less than the previous one.
Hence, it prints backwards.

# Chapter 6, Exercise 2:

A variable with the index[:] includes all characters, and therefore
leaves the string unchanged.

# Chapter 6, Exercise 3:

This function takes a string and a character as arguments.
The number of characters in that string is then counted.

# Chapter 6, Exercise 4:

The .count method does the same thing as my function from chapter 6 exercise 3.

# Chapter 6, Exercise 5:

I had a minor issues with this exercise because I was mixing up .find vs. another method.

# Chapter 6, Exercise 6:

This exercise didn't instruct me to do anything besides to read about string methods:
# https://docs.python.org/3/library/stdtypes.html#string-methods

# Chapter 7, Exercise 1 & 3:

This function prompts the user for an input to find a file.
If the user inputs a file that doesn't exist, it uses
a while loop to send the user an error message until
a valid input is found. It prints the file in all capital letters.
I also added the "easter egg" in my function. 
I've been having issues where my files aren't being found properly
because the files are in another location. 
I don't know how to fix this pernamently, but I've been using
some basic linux commands to change directories to fix my problem.
I also a with as statement to open my file, which I'm not familiar with.
I prefer the open function and close method because it's easier to understand
and you'd have manually control over when you close a file.
If you don't close a file automatically from a function, then you can use that
file as a return value to use in another function.

https://www.geeksforgeeks.org/with-statement-in-python/

# Chapter 7, Exercise 2:

This function basically does the same thing as the previous one.
However, it searches for every line that has "X-DSPAM-Confidence:".
Then it isolates the numbers and converts it from strings to floats,
and finds the average.

# Exercise 1:

This function prompts the user for their given name, and spits back
the first, middle, and last letters in their name.

# Exercise 2:

This function takes two strings as an arguement, and concatrates them.

# Exercise 3:

This function takes a string and a character as arguments. Then it counts
how about characters are in that given string.

# Exercise 4:

This function promotes the user for what file to open and 
If that file doesn't exist or is not found, it repeats itself unless
"nevermind" is typed in. I need to learn how to use functions more effectively
because this function basically does the same thing as my name function.
It only opens files as an extra step. Maybe I could utilize that as a function call in
my nameinfo function.

# Exercise 5:

This function was made specifically to find names in files. However, it could probably
be simplified and utlitize my previous function(s).

# Exercise 6:

This function creates a new file if it doesn't already exist.