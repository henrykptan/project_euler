"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


def is_prime(n):
    if n < 2: return False  # not prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# all(iterable) will return true if all elements of the iterable are True, else False (also any(iterable))

def circular_test(n):
    string_n = str(n)
    digits = [digit for digit in string_n]  # we create a string and then a list of the digits in the prime
    return all(is_prime(int("".join([digits[i - j] for i in range(len(digits))]))) for j in range(len(digits)))


# Sieving to create a list of primes as our iterable makes things a bit quicker

def sieve(n):
    is_primes = [True] * n
    is_primes[0] = False
    is_primes[1] = False
    is_primes[2] = True
    for i in range(3, int(n ** (1 / 2) + 1), 2):
        index = 2 * i
        while index < n:
            is_primes[index] = False
            index += i
    primes = [2]
    for i in range(3, n, 2):
        if is_primes[i]:
            primes.append(i)
    return primes


if __name__ == '__main__':

    count = 0
    for i in sieve(1000000):
        if circular_test(i):
            count += 1
    print(count)
