#Challenge 25: All the Same
def all_the_same(arr):
    return len(set(arr)) == 1

#Extra Challenge: Reverse a String
def read_backwards(s):
    return " ".join(s.split()[::-1])

print(all_the_same(['Mary','Mary','Mary']))
print(all_the_same(['Mary','mary','Mary']))

str1 = 'the love is real'
print(read_backwards(str1))
str1 = "we'll train the train well"
print(read_backwards(str1))
