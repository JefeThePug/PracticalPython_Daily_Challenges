#Challenge 23: Simple Calculator
import re

def get_equation():
    txt = '''Please input a simple maths equation.
      You can use +, -, ×(*), or ÷(/):'''
    return input(txt).replace('×','*').replace('÷','/').rstrip('=')

def calculate():
    equation = get_equation()
    while not re.match(r'^\d+[-+*/]\d+$', equation):
        print("That is not a simple equation. Try again.")
        equation = get_equation()
    try:
        result = eval(equation)
    except ZeroDivisionError:
        return "You cannot divide by zero!"
    else:
        return result 

#Extra Challenge: Multiply Words
from math import prod

def multiply_words(s):
    return prod([len(c) for c in s.split() if c.islower()])

print(calculate())
print(multiply_words('love live and laugh'))
print(multiply_words('Hate war love Peace'))
