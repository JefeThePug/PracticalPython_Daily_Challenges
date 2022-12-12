#Challenge 6: User Name Generator
def user_name():
    return input("Enter your email: ").split("@")[0]

#Extra Challenge: Zero Both Ends
def zeroed_code(nums):
    return [0,*nums[1:-1],0]

print(user_name())

print(zeroed_code([2, 5, 7, 8, 9]))
