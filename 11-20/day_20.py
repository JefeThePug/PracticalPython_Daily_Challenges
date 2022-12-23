#Challenge 20: Capitalize First Letter
def capitalized(s):
    return s.title()

#Extra Challenge: Reversed List
import re

def reversed_list(s):
    pattern = r'\w*[A-Z]\w*'
    return [i[::-1] for i in re.findall(pattern, s)]

print(capitalized('i like learning'))
print(capitalized("i love cheese"))

str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
print(reversed_list(str1))
str1 = 'this will give you nothing'
print(reversed_list(str1))
