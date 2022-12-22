#Challenge 19: Words and Elements
def count_words(s):
    return f'{len(s.split())} words'

def count_elements(s):
    return f'{len(s.replace(" ",""))} elements'

txt = 'I love learning'
print(count_words(txt))
print(count_elements(txt))
