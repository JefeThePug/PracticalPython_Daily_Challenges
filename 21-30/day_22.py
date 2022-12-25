#Challenge 22: Add Under_Score
def add_hash(s):
    return '#'.join(s.split())

def add_underscore(s):
    return s.replace('#','_')

def remove_underscore(s):
    return s.replace('_','')

txt='Python'
print(remove_underscore(add_underscore(add_hash(txt))))

txt='This is a pointless exercise'
print(remove_underscore(add_underscore(add_hash(txt))))
