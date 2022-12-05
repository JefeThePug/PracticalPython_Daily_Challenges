#Challenge 1: Division and Square-root
def divide_or_square(n):
    return n%5 or n**0.5

#Extra Challenge: Longest Value
def longest_value(d):
    return max(d.values(), key=len)

print(divide_or_square(10))
print(divide_or_square(12))
print(longest_value({'fruit':'apple','color':'green'}))
print(longest_value({'fruit':'apple','color':'green','insect':'butterfly'}))
