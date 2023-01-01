#Challenge 29: Middle Figure
from itertools import filterfalse as ff
def middle_figure(a, b):
    s = [*ff(str.isspace, a+b)]
    if len(s)&1:
        return s[len(s)//2]
    return 'no middle figure'

'''
Shorter but less readable:
def middle_figure(a, b):
    s = [*ff(str.isspace, a+b)]
    return s[len(s)//2]*(len(s)&1) or 'no middle figure'
'''

txt1='make love'
txt2='not wars '
print(middle_figure(txt1, txt2))
txt2='not war'
print(middle_figure(txt1, txt2))
txt1='a'
txt2=''
print(middle_figure(txt1, txt2))
