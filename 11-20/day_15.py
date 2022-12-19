#Challenge 15: Same in Reverse
def same_in_reverse(s):
    return s == s[::-1]

#Extra Challenge: What's My Age?
NAMES_AGE = {'jane': 23, 'kerry': 45, 'tim': 34, 'peter': 27}

def your_age(name):
    if name.lower() not in NAMES_AGE:
        print(f"I don't recognise you, {name.title()}")
        NAMES_AGE[name.lower()] = int(input("How old are you?: "))
    return f'Hi, {name.title()}, you are {NAMES_AGE[name.lower()]} years old.'

print(same_in_reverse('dad'))
print(same_in_reverse('dada'))

print(your_age("Tim"))
print(your_age("Jeff"))
print(your_age("Jeff"))
