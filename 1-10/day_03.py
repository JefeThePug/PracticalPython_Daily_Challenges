#Challenge 3: Register Check
def register_check(reg):
    return [x.upper() for x in reg.values()].count('YES')

#Extra Challenge: Lowercase Names
def lower_names(names):
    return tuple(n for n in sorted(names,reverse=True) if n == n.lower())
    
register = {'Michael': 'yes', 'John': 'no', 'Peter': 'Yes', 'Mary': 'Yes'}
print(register_check(register))

names = ['kerry','#','John','Mary','carol','Rose','adam']
print(lower_names(names))
names = ['alice','BETTY','Joan','xarlos']
print(lower_names(names))
