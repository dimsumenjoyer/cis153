'''
Victor Van
00319912
CIS153: Problem Set 8
Professor Penta
11/14/2023, Due: 11/19/2023
'''

# Chapter 12, Exercise 1:

import socket

def input_url():
    input_url = "https://www.overleaf.com/latex/templates/a-quick-guide-to-latex/fghqpfgnxggz" #input("Enter a URL: ")
    try:
        host = input_url.split('/')[2]
        print(f"Host: {host}.") # test
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        cmd = ("GET " + input_url + " HTTP/1.0\r\n\r\n").encode()
        mysock.send(cmd)
        done = False
        while not done:
            data = mysock.recv(512)
            if len(data) < 1:
                done = True
            print(data.decode(), end = "")
        mysock.close()
    except:
        print("Error: Invalid URL.")
    return

#input_url()

# Chapter 12, Exercise 1 & 2:
def display():
    input_url = "http://www.example.com" #"https://www.scientificamerican.com/article/long-covid-now-looks-like-a-neurological-disease-helping-doctors-to-focus-treatments1/" #input("Enter a URL: ")
    try:
        host = input_url.split('/')[2]
        print(f"Host: {host}") # test
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        cmd = ("GET " + input_url + " HTTP/1.0\r\n\r\n").encode()
        mysock.send(cmd)
        done = False
        character_count = 0
        while not done:
            data = mysock.recv(512)
            character_count += 1
            if len(data) < 1 or character_count > 3000:
                done = True
            print(data.decode(), end = "")
        mysock.close()
    except:
        print("Error: Invalid URL.")
    return

display()

# Extra:
# https://developer.spotify.com