#Challenge 39: Password Generator
from random import randint, choices, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def get_distribution(total):
    """
    Returns a list with 4 numbers which sum up to the total passed in.
    
    This list is used to determine the number of lowercase letters, 
    uppercase letters, digits, and symbols that should be used to make
    the password, assuring each password has at least one of each 
    element, and that the quantity of each element is random.
    """
    nums = []
    for i in range(3):
        val = randint(1, total-(3-i))
        nums.append(val)
        total -= val
    nums.append(total)
    return nums

def get_chars(index, number):
    group = [ascii_lowercase, ascii_uppercase, digits, punctuation][index]
    return choices(group, k=number)

def generate_password():
    strength = int(input('Select password strength (0:weak, 1:strong, 2:very strong): '))
    distrib = get_distribution([5,8,12][strength])
    password = sum((get_chars(i,val) for i,val in enumerate(distrib)),[]) #flatten list
    shuffle(password)
    return ''.join(password)

print(generate_password())
