#Challenge 2: Strings to Integers
def convert_add(nums):
    return sum(map(int,nums))

#Extra Challenge: Duplicate Names
def check_duplicates(arr):
    return ', '.join({i for i in arr if arr.count(i)>1}) or "No duplicates"

print(convert_add(['1','20','3']))
print(check_duplicates(['apple', 'orange', 'banana', 'apple', 'orange']))
print(check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark']))
