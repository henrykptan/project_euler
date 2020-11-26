"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


def is_prime(input_num):
    if input_num < 2:
        return False
    else:
        for num in range(2, int(input_num ** (1 / 2)) + 1):
            if input_num % num == 0:
                return False
    return True


def permutation(a, b):
    string_a, string_b = str(a), str(b)
    digits = []
    for i in range(0, len(string_a)):
        digits.append(string_a[i])
    for j in range(0, len(string_b)):
        if string_b[j] not in digits:
            return False
        else:
            digits.remove(string_b[j])
    if not digits:
        return True


primes = []
n = 1
while n < 10000:
    if is_prime(n):
        primes.append(n)
    n += 2

for i in range(0, len(primes)):  # testing any two primes from the list of all primes below a certain value,
    # firstly if they are a permutation of one another
    for j in range(0, i):  # then if the third in the sequence is prime and a permutation
        diff = primes[i] - primes[j]
        if permutation(primes[i], primes[j]):
            if (is_prime(primes[i] + diff)) and \
                    ((primes[i] + diff) in primes) and (permutation(primes[i], primes[i] + diff)):
                print(primes[j], primes[i], primes[i] + diff)
