#Challenge 38: Guess a Number
from random import randint

def guess_a_number():
    correct = randint(1,10)
    for _ in range(3):
        guess = int(input('Guess the number. (1 - 10): '))
        if guess == correct: return 'You have been declared a winner.'
        print('That guess was too', 'high' if guess > correct else 'low')
    return f'The number was {correct}. You have been declared a loser.'

#Extra Challenge: Find Missing Numbers
def missing_numbers(arr):
    return [*set(range(arr[0], arr[-1])).difference(arr)]
    #return [i for i in range(arr[0], arr[-1]) if i not in arr]

print(guess_a_number())

a = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
print(missing_numbers(a))
a = [2, 23]
print(missing_numbers(a))
