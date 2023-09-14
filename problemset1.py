'''
Victor Van 9/11/2023
Problem Set 2 - Due: 9/18/2023
Exercises 1-5 from Problem Set 2.
Outside Resources: I used google for the equation to convert Celsius to Fahrenheight.
'''

# Exercise 1:
'''Integers (and floats), such as 5, need to either be stored in a varible
or printed out. It can't just type an integer by itself like this:
5
'''
try:
    5
except:
    print("Error: 5 isn't stored into a varible.")
    
x = 5 # sets a varible "x" = to an integer 5
x = x + 1 # takes the varible x which is = 5 and adds 1
#print(x) # x = 5; therefore x = x + 1 is equal to 6

# Exercise 2:

def name():
    y = input("Enter your name: ")
    print("Hello " + y)
#name()
    
# Exercise 3:

def salary():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = hours * rate
    print("Pay: " + str(pay))
#salary()

# Exercise 4:

width = 17
height = 12.0

modulus_operator = width//2
#print(width//2) # outputs 8
#print(type(modulus_operator)) # varible type: integer

division_1 = width/2
#print(width/2.0) # outputs 8.5
#print(type(division_1)) # varible type: float

division_2 = height/3
#print(division_2) # outputs 4.0
#print(type(division_2)) # outputs float

victor_is_cool = 1 + 2 * 5
#print(victor_is_cool) # outputs 11
#print(type(victor_is_cool)) # varible type: integer

# Exercise 5:

def celsius_to_fahrenheit():
    celsius = float(input("What is the temperature in Celsius?: "))
    fahrenheit = (9/5) * celsius + 32
    print("The converted temperature is " + str(fahrenheit) + " degrees Fahrenheit.")

#celsius_to_fahrenheit()

#_____________________________________________________________________________________________________
# For myself:

def fahrenheit_to_celsius():
    fahrenheit = float(input("What is the temperature in Fahrenheit?: "))
    celsius = ((fahrenheit - 32) * 5) / 9
    print("The converted temperature is " + str(celsius) + " degrees Celsius.")
    
fahrenheit_to_celsius()