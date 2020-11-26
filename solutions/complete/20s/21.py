"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the SUM of all the amicable numbers under 10000.
"""
import math
import time

start = time.time()


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


def calculate_amicable_pairs(n):
    """
    We create a list of the sum of the divisors of each of the numbers in our range
    Then for each number we test if the divisor_sum is
    """
    divisor_sum_list = [calculate_divisor_sum(i) for i in range(n + 1)]
    pairs = []
    for i in range(n + 1):
        divisor_sum = divisor_sum_list[i]
        if i < divisor_sum <= n and divisor_sum_list[divisor_sum] == i:
            pairs.append([i, divisor_sum])
    return pairs


def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])


if __name__ == '__main__':
    print("Solution is {} found in time {}".format(sum_pairs(calculate_amicable_pairs(10000)), time.time() - start))
