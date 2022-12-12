#Challenge 8: Odd and Even
def odd_even(nums):
    odds = {n for n in nums if n%2}
    evens = set(nums).difference(odds)
    return max(evens) - min(odds)

#Extra Challenge: List of Prime
def sieve(n):
    primes = 2*[False] + (n-1)*[True]
    for i in range(2, int(n**0.5 + 1)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, is_true in enumerate(primes) if is_true]

def prime_numbers():
    n = int(input("Enter a number: "))
    if n < 2: return []
    return sieve(n)

print(odd_even([1,2,4,6]))
print(odd_even([1,2,3,4,5,6,7,8,9,10]))
print(odd_even([2,9,11]))

print(prime_numbers())
