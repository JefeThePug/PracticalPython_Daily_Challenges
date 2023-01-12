#Challenge 40: Pig Latin
def find_vowel(word):
    if word[0].lower() in 'aeiou': return 0
    for i,c in enumerate(word[1:], 1):
        if c.lower() in 'aeiouy': return i

def piglatin_translate(s):
    result = []
    for word in s.split():
        i = find_vowel(word)
        result.append(word[i:] + word[:i] + ('ay' if i else 'yay'))
    return ' '.join(result)

'''
I changed the rules of the challenge slightly to more correctly reflect
how pig latin is translated: namely words begining with a consonant blend,
like 'br' or 'th', should have the entire blend moved to the end rather
than only the first letter like the challenge suggests.
For example: 'thread'
according to the rules of the challenge, you would get 'hreadtay'
but with the more complex rules of pig latin you should get 'eadthray'
'''

print(piglatin_translate('i love python'))
print(piglatin_translate('yes they love python'))
print(piglatin_translate('it was the best of times it was the worst of times'))
