def index_position(s):
    return [i for i,c in enumerate(s) if c.islower()]

#Extra Challenge: Largest Number
def largest_number(nums):
    return int("".join(sorted("".join(map(str,nums))))[::-1])

print(index_position('LovE'))
print(index_position('LOVE'))

list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))
list1 = [9991,992,94,93]
print(largest_number(list1))
