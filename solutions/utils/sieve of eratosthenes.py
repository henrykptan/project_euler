"""
prime number finding function - sieve of Eratosthenes
way way way way quicker when generating a really large set of primes
"""
import time

start = time.time()


def sieve(n):
    is_prime = [True] * n  # create an list of n trues
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated (when we generate)
    for i in range(3, int(n ** 0.5 + 1), 2):  # so we check the odds
        index = i * 2
        while index < n:  # we now go through every odd number up to sqrt(n)+1, and remove its multiples lower than n
            is_prime[index] = False
            index += i
    primes = [2]
    for i in range(3, n, 2):  # we then generate our set of primes (note no need to check evens after 2)
        if is_prime[i]:
            primes.append(i)
    return primes


def divisors(n):
    primes = [2]
    for i in range(3, n, 2):
        test = True
        for j in range(2, i):
            if i % j == 0:
                test = False
        if test:
            primes.append(i)


print(sieve(1000))
