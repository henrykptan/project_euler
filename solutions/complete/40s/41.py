"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?

Note must be less than 987654321 by the definition of pandigital
"""
from math import sqrt, ceil


def sieve(n):  # sieve of eratosthenes
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(3, ceil(sqrt(n)) + 1, 2):  # iterate through the odd numbers, eliminating multiples
        index = 2 * i
        while index < n:
            is_prime[index] = False
            index += i
    primes = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)
    return primes


def is_pandigital(n):
    string_n = str(n)
    nums = sorted([int(digit) for digit in string_n])
    if nums == [i for i in range(1, len(string_n) + 1)]:
        return True
    else:
        return False


if __name__ == '__main__':

    test = 987654321

    prime_list = sieve(test)
    for prime in prime_list:
        if is_pandigital(prime):
            print(prime)
