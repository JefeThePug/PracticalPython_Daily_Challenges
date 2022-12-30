#Challenge 27: Unique Numbers
def unique_numbers(s):
    if (sum(s) - sum(u:=set(s)))&1:
        return [*u]
    return s

#Extra Challenge: Difference of Two Lists
def difference_of_two(a,b):
    return [n for n in a+b if (a+b).count(n)==1]

print(unique_numbers([1,2,4,5,6,7,8,8]))
print(unique_numbers([1,2,5,5,6,7,8,8]))

a=[1,2,4,5,6]
b=[1,2,5,7,9]
print(difference_of_two(a,b))
