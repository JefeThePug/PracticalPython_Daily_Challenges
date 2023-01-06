#Challenge 34: Just Digits
import csv

def just_digits():
    with open('day_34_python.csv', 'r') as raw_data:
        words = raw_data.read().split()
        return [i for i in words if i.isdigit()]

print(just_digits())
