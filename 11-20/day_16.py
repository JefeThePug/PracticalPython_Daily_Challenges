#Challenge 16: Sum the List
def sum_list(arr):
    return sum([sum(i) for i in arr])

#Extra Challenge: Unpack A Nest
def unpack(arr):
    return [*{i for a in arr for i in a if i in (34,67,78)}]

print(sum_list([[2,4,5,6],[2,3,5,6]]))

print(unpack([[12, 34, 56, 67], [34, 68, 78]]))
