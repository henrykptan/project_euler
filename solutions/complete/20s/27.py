"""
Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of nn
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""


# n = 0 -> b must be prime
# n = 1 -> a must be odd


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


def is_in_prime_list(n, prime_list):
    return n in prime_list


def quadratic_is_prime(a, b, n, prime_list):
    return is_in_prime_list(n * n + a * n + b, prime_list)


def number_of_consecutive_quadratic_primes(a, b, prime_list):
    n = 0
    while quadratic_is_prime(a, b, n, prime_list):
        n += 1
    return n


if __name__ == "__main__":

    primeList = sieve(1000000)

    testPrimes = [num for num in primeList if num <= 1000] + [-num for num in primeList if num <= 1000]

    for i in testPrimes:
        for j in testPrimes:
            no = number_of_consecutive_quadratic_primes(i, j, primeList)
            if no > 10:
                print(i, j, no)
