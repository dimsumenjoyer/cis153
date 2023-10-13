'''
Victor Van 00319912
Problem Set 5
Chapters 6 & 7
Professor Penta
10/2/2023, Due: 10/9/2023
'''
# Chapter 6, Exercise 1:

def print_backwards():
  x = 0
  user_input = input("Enter something to print backwards: ") #input fruit
  length = len(user_input)
  while x < length:
      if length == 0:
          break
      length -= 1
      letter = user_input[length]
      print(letter)
  print("Done!")
  return

#print_backwards()

# Chapter 6, Exercise 2:

fruit = "fruit"
#print(fruit[:]) # fruit [:] means all characters in the varible fruit

# Chapter 6, Exercise 3:

def count(string, letter):
   count = 0
   x = 0
   y = len(string)
   while x < y:
      if string[x] == letter:
         count += 1
      x += 1
   return count

banana_a = count("banana", "a")
#print(banana_a)

# Chapter 6, Exercise 4:
banana = "banana"
#print(banana.count("a"))

# Chapter 6, Exercise 5:

string = "X-DSPAM-Confidence: 0.8475"
colon = string.find(":")
uncleaned_num = string[colon + 1:]
string_num = uncleaned_num.strip()
float_num = float(string_num)
#print(float_num)

# Chapter 6, Exercise 6:

# https://docs.python.org/3/library/stdtypes.html#string-methods

# Chapter 7, Exercise 1 & 3:

# https://www.py4e.com/code3/mbox-short.txt

def textfile():
   done = False
   while not done:
      try:
         user_input = input("Enter a file name: ") # mbox-short.txt
         if user_input == "na na boo boo":
            print("NA NA BOO BOO TO YOU - You have been punk'd!")
         elif user_input == "nevermind":
            print("Sorry.")
            done = True
            break
            # https://www.py4e.com/code3/mbox-short.txt
            # https://www.geeksforgeeks.org/with-statement-in-python/
         with open(user_input) as textfile_obj:
            print(textfile_obj)
            for line in textfile_obj:
               print(line.strip().upper())
         done = True
         break
      except FileNotFoundError:
         print("Error: File Not Found. Please try again.")
         continue
      return

textfile()

# Chapter 7, Exercise 2:

def extract_average():
   #user_input = input("Enter a file name: ")
   user_input = "mbox-short.txt"
   total = 0
   iteration = 0
   with open(user_input) as textfile_obj:
      for line in textfile_obj:
         if line.startswith("X-DSPAM-Confidence:"):
            colon = line.find(":")
            numbers = float(line[colon + 1:])
            total += numbers
            iteration += 1
   average = (total/iteration)
   print(f"Average: {average}") 
   return

#extract_average()

# :(

# Exercise 1:

def name():
   user_input = input("What is your given name?: ")
   first_letter = user_input[0]
   name_length = len(user_input)
   last_letter = user_input[name_length-1]
   middle_letter_value = int(name_length/2)
   middle_letter = user_input[middle_letter_value]
   print(f"Your name is {user_input}. The first letter is {first_letter}, middle letter {middle_letter}, and last latter {last_letter}.")
   return

#name()

# Exercise 2:
def concentration(string1, string2):
   print(f"{string1} {string2}")
   return

#concentration("fuck", "you")

def name():
   user_input = input("What is your given name?: ")
   first_letter = user_input[0]
   name_length = len(user_input)
   last_letter = user_input[name_length-1]
   middle_letter_value = int(name_length/2)
   middle_letter = user_input[middle_letter_value]
   print(f"Your name is {user_input}. The first letter is {first_letter}, middle letter {middle_letter}, and last latter is {last_letter}.")
   return

#name()

# Exercise 2:
def concentration(string1, string2):
   print(f"{string1} {string2}")
   return

#concentration("fuck", "you")

# Exercise 3:
def character_count(string, character):
  string_lower = string.lower()
  character_lower = character.lower()
  count = string_lower.count(character_lower)
  print(f"There are {count}s {character} in {string}.")
  return count 

#character_count("Victor Van", "V")

# Exercise 4:
def filename():
   user_input = input("What file do you want to open?: ")
   file = open(user_input)
   for name in file:
      first_letter = name[0]
      name_length = len(name)
      last_letter = name[-1]
      middle_letter_value = int(name_length//2)
      middle_letter = name[middle_letter_value]
      print(f"Your name is {name}. The first letter is {first_letter}, middle letter {middle_letter}, and last latter {last_letter}.")
   return

# Exercise 5:

def findnames():
   user_input = input("What file do you want to open?: ") #names.md
   done = False
   while not done:
      if user_input == "nevermind":
         print("Sorry.")
         done = True
         break
      try:
         file = open(user_input)
         for name in file:
            print(name)
         file.close()
         done = True
         break
      except FileNotFoundError:
         print("Error: File Not Found. Please try again.")
         continue
   return

#findnames()

# Exercise 6:

def findnames():
   user_input = input("What file do you want to open?: ") #names.md
   done = False
   while not done:
      if user_input == "nevermind":
         print("Sorry.")
         done = True
         break
      try:
         file = open(user_input)
         for name in file:
            print(name)
         file.close()
         done = True
         break
      except FileNotFoundError:
         print("Error: File Not Found. Please try again.")
         continue
   return

#findnames()

# Exercise 6:

def outputfile():
   print("Note File: ")
   user_input = input()
   file = open("outputfile.md", "w")
   file.write(user_input)
   file.close()
   return

#outputfile()
