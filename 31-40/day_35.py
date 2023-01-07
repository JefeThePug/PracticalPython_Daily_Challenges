#Challenge 35: Pangram
from string import ascii_lowercase

def check_pangram(s):
    return not set(ascii_lowercase).difference(s)

#Extra Challenge: Find my Position
def find_index(arr, i):
    return [x for x,n in enumerate(arr) if n == i] or [i]*len(arr)

print(check_pangram('the quick brown fox jumps over a lazy dog'))
print(check_pangram('Mary had a little lamb whose fleece was white as snow'))

print(find_index([1, 2, 4, 6, 7, 7], 7))
print(find_index([1, 2, 4, 6, 7, 7], 8))
