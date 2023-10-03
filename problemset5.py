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

str = "X-DSPAM-Confidence: 0.8475"
colon = str.find(":")
uncleaned_num = str[colon + 1:]
string_num = uncleaned_num.strip()
float_num = float(string_num)
#print(float_num)

# Chapter 6, Exercise 6:

# https://docs.python.org/3/library/stdtypes.html#string-methods

# Chapter 7: Exercise 1:

# https://www.py4e.com/code3/mbox-short.txt