#Challenge 33: List Intersection
def inter_section(a, b):
    return *set(a).intersection(b),
    

#Extra Challenge: Set or List
from timeit import timeit

def set_or_list(rng, n):
    code = f'{n} in {list(range(rng))}'
    time_list = timeit(code, number = 100)
    code = f'{n} in {set(range(rng))}'
    time_set = timeit(code, number = 100)
    print(f'{time_list = } seconds\n{time_set = } seconds'.replace('time_',''))
    
    return f'{"Set" if time_set<time_list else "List"} is faster'

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1, list2))

print(set_or_list(1000000, 999999))
print(set_or_list(100, 100))
