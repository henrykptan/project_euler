"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
from math import sqrt


def sieve(n):
    is_prime_list = [True] * n
    is_prime_list[0] = False
    is_prime_list[1] = False
    is_prime_list[2] = True
    for i in range(3, int(sqrt(n) + 1), 2):
        index = 2 * i
        while index < n:
            is_prime_list[index] = False
            index += i
    prime_list = [2]
    for i in range(3, n, 2):
        if is_prime_list[i]:
            prime_list.append(i)
    return prime_list


if __name__ == '__main__':
    start = time.time()
    primes = sieve(1000000)
    print(primes[10000])
