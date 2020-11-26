"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


# first create the set of primes less than or equal to the desired number, as the total must be some product of
# powers of these primes by the fundamental theorem of arithmetic
# Then our solution must be something that looks like 2^p1 + 3^p2 + ... + 19^p8 , where pi > 0 for all i

def is_prime(m):
    if m < 2:
        return False
    else:
        for j in range(2, m):
            if m % j == 0:
                return False
        return True


if __name__ == '__main__':
    num = 20
    primes = [n for n in range(0, num + 1) if is_prime(n)]

    # now must go through powers of the primes until the value produced is more than num
    powers = []

    for prime in primes:
        # for each prime x, find the highest power such that x^p is less than our number
        # this will cross off being divisible by all ints below 20
        power = 1
        while prime ** power <= num:
            power = power + 1
        powers.append(power - 1)

    ans = 1
    for i in range(0, len(primes)):
        ans = ans * (primes[i] ** powers[i])

    print(ans)
