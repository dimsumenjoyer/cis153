'''
Victor Van
CIS153: Problem Set 6
Professor Penta
10/23/2023, Due: 11/7/2023
'''

def mbox_file():
    with open("mbox-short.txt", "r") as file:
        file.read()
        return file

#mbox_file()

# Chapter 9, Problem 3:

def find_emails():
    email_directionary = {} # {email, number of references}
    with open("mbox-short.txt", "r") as file:
        for line in file:
            if line.startswith("From "):
                split_line = line.split()
                email = split_line[1]
                if email not in email_directionary:
                    email_directionary[email] = 1
                else:
                    email_directionary[email] += 1
    return email_directionary
    
print(find_emails())

# Chapter 9, Problem 4:

#print(emails)
#email_values = emails.values()
#print(email_values)

def mail_log(email_directionary):
    topemail = ""
    most_messages = 0
    for value in email_directionary:
        count = email_directionary[value]
        mail = ""
        if count > most_messages:
            most_messages = count
            # topemail =
    return most_messages

print(mail_log(find_emails())

#most_messages()

# Chapter 9, Problem 5:
def email_addresses():
    print(emails)
    return emails

#email_addresses()

# Chapter 10, Problem 1:

# Chapter 10, Problem 2:
