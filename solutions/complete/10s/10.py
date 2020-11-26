"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# SIEVE OF ERATOSTHENES
import time

start = time.time()


def sieve(n):
    """
    produce a list of primes up to the number n
    """
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # we then go through each odd number and delete its multiples (note evens we know not to be prime)
    for i in range(3, int(n / 2 + 1), 2):
        index = i * 2  # we start by eliminating the 2nd multiples and go from there
        while index < n:
            is_prime[index] = False
            index += i
            # then we create our list
    primes = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)
    return primes


if __name__ == '__main__':
    ans = 0
    for prime in sieve(2000000):
        ans += prime

    print("ans is {} found in time {}".format(ans, time.time() - start))
