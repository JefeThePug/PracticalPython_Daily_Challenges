#Challenge 30: Most Repeated Name
from collections import Counter
def repeated_name(arr):
    return Counter(arr).most_common()[0][0]

"""
without Counter:
def repeated_name(arr):
    counts = [(n,arr.count(n)) for n in set(arr)]
    return max(counts, key=lambda x:x[1])[0]
"""

#Extra Challenge: Sort by Last Name
def swap_items(arr):
    return sorted(f'{b} {a}'for a,b in map(str.split, arr))

names = ['John','Peter','John','Peter','Jones','Peter']
print(repeated_name(names))

names = ['Beyonce Knowles','Alicia Keys','Katie Perry','Chris Brown','Tom Cruise']
print(swap_items(names))
