#Challenge 44: Save Emails
import csv #just for fun, trying this using the csv module

def save_emails():
    with open('day_44_emails.csv', 'w') as file:
        writer = csv.writer(file)
        while True:
            email = input('Enter email or "done" to finish: ')
            if email.lower().replace('"','').strip() == 'done': break
            writer.writerow([email])

def open_emails():
    with open('day_44_emails.csv', 'r') as file:
        reader = [''.join(line) for line in csv.reader(file)]
        return ' '.join(reader)


#Probably better to ignore the csv aspect of this and do it with just a file.
'''
def save_emails():
    with open('day_44_emails.csv', 'w') as file:
        while True:
            email = input('Enter email or "done" to finish: ')
            if email.lower().replace('"','').strip() == 'done': break
            file.write(email + '\n')

def open_emails():
    with open('day_44_emails.csv', 'r') as file:
        return file.read()
'''

save_emails()
print(open_emails())
