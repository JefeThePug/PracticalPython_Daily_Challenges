#Challenge 32: Password Validator
def password_validator():
    while True:
        issues = ''
        pwd = input('Enter a password: ')
        if not any(c.isupper() for c in pwd):
            issues += 'You must include at least one uppercase letter.\n'
        if not any(c.islower() for c in pwd):
            issues += 'You must include at least one lowercase letter.\n'
        if not any(c.isdigit() for c in pwd):
            issues += 'You must include at least one number.\n'
        if len(pwd) < 7:
            issues += 'Your password must be at least 8 characters long.\n'
        if not issues:
            return pwd
        print(issues, 'Please enter a valid password.', sep="")


#Extra Challenge: Valid Email
import re

def email_validator(emails):
    matches = [e for e in emails if re.match(r'\w+@\w+\.com', e)] 
    return matches or 'all emails are invalid'

print(password_validator())
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
print(email_validator(emails))
emails = ['b@en@mail.com', 'john@mail.cm', 'kenny@.com', '@list.com']
print(email_validator(emails))
