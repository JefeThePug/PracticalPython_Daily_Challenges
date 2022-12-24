#Challenge 21: List of Tuples
def make_tuples(a, b):
    return list(zip(a,b))

#Extra Challenge: Even Number or Average
def even_or_average(nums):
    evens = [n for n in nums if not n&1]
    return max(evens) if evens else sum(nums)/len(nums)

print(make_tuples([1,2,3,4],[5,6,7,8]))

print(even_or_average([1,2,3,4,5]))
print(even_or_average([1,3,5,7,9]))