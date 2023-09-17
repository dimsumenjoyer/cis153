'''
Victor Van
Programming for IT (Python)
Professor Michael Penta
Problem Set 4 Exercises 1-2
9/16/2023, Due: 10/9/2023
'''

# Exercise 1:

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

# Exercise 2:

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