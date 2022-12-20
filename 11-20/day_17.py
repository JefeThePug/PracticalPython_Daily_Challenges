#Challenge 17: User Name Generator

from random import randint

def user_name(name):
    return f'{name[::-1].lower()}{randint(0,9)}'

#Extra Challenge: Sort by Length

def sort_length(names):
    # boo why not use built-in sort?? >>> return sorted(names, key=len)
    ref = {}
    for name in names:
        ref.setdefault(len(name), []).append(name)
    output = [ref[i] for i in range(max(ref.keys())+1) if i in ref]
    return sum(output, []) #flattens the list of lists
                   

print(user_name('chiaki'))
print(user_name('Xarlos'))

print(sort_length( ['Peter','Jon','Andrew']))
print(sort_length( ['Peter','Jon','Frank','Andrew']))
