#Challenge 10: Hide My Password
def hide_password(pwd):
    return f'{"*"*len(pwd)} : Password is {len(pwd)} characters long.'

#Extra Challenge: A Thousand Separator
def add_separator(nums):
    return [f'{num:,}' for num in nums]

print(hide_password())
print(add_separator([1000000, 2356989, 2354672, 9878098]))
