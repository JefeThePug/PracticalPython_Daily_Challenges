#Challenge 37: Count the Vowels

#if lowercase vowels and uppercase vowels should be considered different...
def count_the_vowels_a(s):
    return len(set('AEIOUaeiou').intersection(s))

#if lowercase vowels and uppercase vowels should be considered the same...
def count_the_vowels_b(s):
    return len(set('aeiou').intersection(s.lower()))

print(count_the_vowels_a('saas')) # >>>1
print(count_the_vowels_a('sous')) # >>>2
print(count_the_vowels_a('sAas')) # >>>2
print(count_the_vowels_a('abcdefghijklmnopqrstuvwxyz')) # >>>5
print(count_the_vowels_a('AEIOUaeiou')) # >>>10

print(count_the_vowels_b('saas')) # >>>1
print(count_the_vowels_b('sous')) # >>>2
print(count_the_vowels_b('sAas')) # >>>1
print(count_the_vowels_b('abcdefghijklmnopqrstuvwxyz')) # >>>5
print(count_the_vowels_b('AEIOUaeiou')) # >>>5
