#Challenge 9: Biggest Odd Number
def biggest_odd(nums):
    return max([int(i) for i in nums if int(i)%2])

#Extra Challenge: Zeros to the End
def zeros_last(arr):
    zeros = [0] * arr.count(0)
    return [*filter(None, arr)] + zeros if zeros else sorted(arr)

print(biggest_odd("23569"))
print(biggest_odd("246810"))
print(zeros_last([1, 4, 8, 7, 9, 0, 0]))
print(zeros_last([2, 1, 4, 7, 6]))
