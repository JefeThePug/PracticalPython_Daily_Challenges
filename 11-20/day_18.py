#Challenge 18: Any Number of Arguments
def any_number(*args):
    return sum(args)/len(args)

#Extra Challenge: Add and Reverse
def add_reverse(a, b):
    if len(a) != len(b): 
        return "the lists are not of equal lengths"
    return [*map(sum,zip(a,b))][::-1]

print(any_number(12,90,12,34))
print(any_number(12,90))
print(any_number(12.33,1))

print(add_reverse([10, 12, 34],[12, 56, 78]))
print(add_reverse([1],[90,100,55]))
