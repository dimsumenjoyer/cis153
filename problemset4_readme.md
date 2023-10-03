'''
Victor Van
Programming for IT (Python)
Professor Michael Penta
Problem Set 4, Chapter 5
9/14/2023, Due: 10/2/2023
'''

# Exercise 1: Write a problem which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and
average of the numbers. If the user enters anything other than a number, detect their message using try and except and print an error message and
skip to the next level.

I made a function called average_number. I made a lot of issues, especially with infinite while loops. A friend recommended me to start using
booleans as a kind of "control variable" to prevent infinfite while loops from occuring. I also had issues with indentations and calling variables
before they were being locally defined. I also had issues with my except statement with what kind of arguments it accepted.
input_string == float and input_string != "done" seem to result in boolean values (True or False) which are not valid arguments.
There's just a litany of issues with my original code.

As an example here is my original code:

def average_number():
    count = 0
    total = 0
    average = 0
    while True:
        input_string = input("Enter a number: ")
        try:
            input_number = float(input_string)

            if input_number == float:
                total += input_number
                count += 1
                average += (total / count)
            elif input_string == "done":
                print("Cumulative Number(s): " + str(total))
                print("Total Count: " + str(count))
                print("Average Number: " + str(average))
                print("Done.")
                break
        except input_string == float and input_string != "done":
                print("Error: Non-Numeric Input. Please enter a number.")
                continue

average_number()

I made to rewrite my code several times from scartch, as well as implement boolean values to prevent while loops from infinitely repeating.
I had to also had to search up what ValueError meant to be able to account for non-numeric inputs that aren't "done".
Another friend also pointed out that I unindenting my print statements at the end would not declare varaiables before calling them
which I was initially reluctant to do because of it. Indenting my print statements one more time would put it inside the while loop,
and therefore have those print statement repeat for every iteration of the while loop.

def average_number():
    count = 0
    total = 0
    average = 0
    done = False
    while not done:
        input_string = input("Enter a number: ")

        # execute while loop
        if input_string == "done":
            done = True
            break

        try:
            input_number = float(input_string) # convert to float
        except ValueError:
            print("Error: Non-numeric Input. Please enter a number.") # fail safe
            continue

        # calculations
        total += input_number
        count += 1
        average = (total / count)

    print("Cumulative Number: " + str(total))
    print("Total Count: " + str(count))
    print("Average Number: " + str(average))
    print("Done.")

#average_number()

______________________________________________________________________________________________________________________________________________________
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Emter a number: 7
Enter a number: done
16 3 5.333333333333333

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers
instead of the average.

I also made this program a function, called minmax_number. I found that with this specific program, it was best to use an empty list.
Later on, a list of floats are appended to it before the minimum and maximum numbers are printed out. Moreover, I also had to use booleans to help
prevent an infinitely repeateding while loop. I also had to search up what ValueError really meant for my exception statement. At the end,
I made a for loop to check if there were any numbers added to the list "numbers". If there weren't, it would return "Error. No valid numbers."
Otherwise, it checks the list "numbers" for their respective minimum and maximum values and prints them.

def minmax_number():
    numbers = []
    done = False
    while not done:
        input_string = input("Enter a number: ")
        if input_string == "done":
            done = True
            break
        try:
            input_number = float(input_string)
            numbers.append(input_number)
        except ValueError:
            print("Error: Invalid input. Enter a number.")
            continue
    if numbers:
        min_number = min(numbers)
        max_number = max(numbers)
        print("Minimum Number: " + str(min_number) + ".")
        print("Maximum Number: " + str(max_number) + ".")
    else:
        print("Error: No valid numbers.")

#minmax_number()
