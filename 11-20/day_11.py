#Challenge 11: Are They Equal?
def equal_strings(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

#Extra Challenge: Swap Values
def swap_values(arr):
    if not arr: return []
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr

print(equal_strings("love", "evol"))
print(equal_strings("Live", "eVIL"))

print(swap_values([2,4,67,7]))
print(swap_values([9]))
