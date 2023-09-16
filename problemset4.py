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


# Exercise 2:
'''
def minmax_number():
    while True:
        input_string = input("Enter a number: ")
        if input_string == "done":
            print("Done.")
            break
        try:
            input_number = float(input_string)
        except ValueError:
            print("Invalid input.")
            continue

minmax_number()
'''