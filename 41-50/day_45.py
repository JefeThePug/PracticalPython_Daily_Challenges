#Challenge 45: Words & Special Characters
from string import punctuation, whitespace
def analyse_string(s):
    s = s.replace('.', '')
    special = len([i for i in s if i in punctuation])
    words = len([i for i in s.translate(s.maketrans('','',punctuation)).split() if not i.isnumeric()])
    total = len([i for i in s if i not in whitespace])
    return {'special character':special,'words':words,'total characters':total}
         

s= 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".'
print(analyse_string(s))

_ = '''
This is without a doubt the worst challenge yet.  
Totally unclear about what constitutes a word 
especially with an example sentence that's packed 
with mathematical expressions and programming 
that include words in various forms.
Is spam=%s one word?  or is spam and s two words?
Is C (the programming language) a word? 
Is printf a word even though it is not actually a word?
What about e.g.?  This was frustrating and I do not 
care if the results are incorrect.  I made my own rules.
'''
