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
    
#print(find_emails())

# Chapter 9, Problem 4:

def mail_log(email_directionary):
    topemailer = ""
    leastemailer = ""
    most_messages = 0
    least_messages = 1000000
    for email, count in email_directionary.items():
        if count > most_messages:
            most_messages = count
            topemailer = email
            emailer_most_messages = f"{topemailer} has the most messages with {most_messages} of them."
        if count < least_messages:
            least_messages = count
            leastemailer = email
            emailer_least_messages = f"{leastemailer} has the least messages with {least_messages} of them."
    return emailer_most_messages, emailer_least_messages

#print(mail_log(find_emails()))

#most_messages()

# Chapter 9, Problem 5:
def email_addresses(email_directionary):
    for email in email_directionary.items():
        print(email)
    #emails = email_dictionary.key()
    return email

#print(email_addresses)

# Chapter 10, Problem 1:
def from_emailaddress():
    file = open("mbox-short.txt", "r")
    email_from = {}
    emails = []
    email = ""
    info = []
    most_commits = ""
    for line in file:
        if line.startswith("From ") or line.startswith("From: "):
            line = line[5:].strip().split()
            email = line[0]
            if email is not None:
                emails.append(email)
    #print(emails) # test
    file.close()
    email_from = {email: emails.count(email) for email in emails}
    info = max(email_from, key = email_from.get)
    return email_from, info

#print(from_emailaddress())
# I don't know how to find the highest value in the dictionary and print out the correspending email.
            
# Chapter 10, Problem 2:


def hour_in_emails():
    file = open("mbox-short.txt", "r")
    time = 0
    for line in file:
        if line.startswith("From ") or line.startswith("From: "):
            line = line[5:].strip().split()
            time = line[5]
            print(time) # test
    return
# I can't isolate time because some the lists are out of range, and I don't know how to deal with that.
hour_in_emails()