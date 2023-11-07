'''
Victor Van
CIS153: Problem Set 6
Professor Penta
11/7/2023, Due: 11/7/2023
'''

I had a lot of issues with this problem set because I spent a lot of time and energy focusing on project 2.

However, most of this problem set is string parsing and then storing them in dictionaries and lists.
I used the .items() on my dictionaries a lot, which puts elements in the dictionary in a list. 
Then you can use list[number] to isolate those elements.
However, I had issues with finding the time in the last problem because my lines varied in length.
The time would be the 5th spot in the list, but not all lists have the same length. 
I don't know how to account for that, and I like to figure things out myself so I unfortunately have not finished this problem set
to a reasonable standard. 
Edit: I figured it out, but I printed our hours in tuples which might not be what I'm exactly looking for but it's close.

For chapter 10, problem 1, I did manage to fufill the requirements.
However, my formatting is a bit weird.
I have a dictionary inside a list, and the email with the highest value is also in the list but not in the dictionary.

Professor Penta also helped me with dictionaries, for instance:
if email not in email_directionary:
    email_directionary[email] = 1
I've also used a dictionary comprehension on 79.

Outside resources:
https://www.w3schools.com/python/ref_dictionary_get.asp
(Side note, I didn't know that the .get method could omit the parenthesis and still work.)
https://realpython.com/sort-python-dictionary/