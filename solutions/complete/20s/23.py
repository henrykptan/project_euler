"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math
import time


def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n and i != 1:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor


def calculate_divisor_sum(n):
    return sum(divisor_generator(n))


def is_abundant(n):
    return calculate_divisor_sum(n) > n


if __name__ == '__main__':

    start = time.time()

    abundants = set()  # note sets have a smaller memory complexity than lists
    limit, total = 28123, 0

    for num in range(1, limit + 1):
        if is_abundant(num):
            abundants.add(num)
        if not any((num - a in abundants) for a in abundants):
            total += num

    print("answer is {}, found in time {}".format(total, time.time() - start))
