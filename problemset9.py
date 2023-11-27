'''
Victor Van
00319912
CIS153: Problem Set 9
Professor Penta
11/26/2023, Due: 11/30/2023
'''

import tkinter as tk

# https://docs.python.org/3/library/tkinter.html

message = tk.Tk()
message.title("message")
label = tk.Label(message, text = "Click for message")

def display_screen():
    label.config(text = "Hello darkness, my old friend \n I've come to talk with you again")
    return

hello_button = tk.Button(message, text = "click here", command = display_screen)
label.pack(pady = 10)
hello_button.pack()

#message.mainloop()

sigma =  tk.Tk()
sigma.title("Summation")

label2 = tk.Label(sigma, text = "Enter two numbers")
user_input1 = tk.Entry(sigma)
user_input2 = tk.Entry(sigma)

def basically_a_summation():
    get_user_input1 = float(user_input1.get())
    get_user_input2 = float(user_input2.get())
    sum_stuff = get_user_input1 + get_user_input2
    label2.config(text = f"Sum: {sum_stuff}")
    return

sum_button = tk.Button(sigma, text = "Calculate Sum", command = basically_a_summation)
label2.pack(pady = 10)
user_input1.pack(pady = 10)
user_input2.pack(pady = 10)
sum_button.pack()

sigma.mainloop()