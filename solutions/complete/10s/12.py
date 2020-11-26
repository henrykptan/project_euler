"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

NOTE nth triangular number formula (n(n+1))/2
"""


def get_triangular_number(num):
    return int((num * (num + 1)) / 2)


def num_divisors(n):
    """
    First we find the divisibility by 2 inc. n, eg for 28 we have (28, 14, 7), so 3 factors
    Then go through the odds, and for each odd that divides  k times, multiply the number of factors by another k+1
    eg 7 is not divisible by 3, 5, but is by 7 -> (28, 14, 7) (4, 2, 1), we multiply the total by (1+1) times
    Then when we get to 1 we have checked off all factors.
    """
    divisor_count = 1
    while n % 2 == 0 and n != 1:
        n = int(n / 2)
        divisor_count += 1
    p = 3
    while n != 1:
        odd_divisor_count = 0
        while n % p == 0:
            odd_divisor_count += 1
            n = n / p
        divisor_count = divisor_count * (odd_divisor_count + 1)
        p += 2
    return divisor_count


if __name__ == '__main__':
    total = 500
    index = 1
    while num_divisors(get_triangular_number(index)) < total:
        index += 1
    triangle = get_triangular_number(index)
    print('Triangular index {}, triangular number {}, number of divisors {}'.format(index, triangle,
                                                                                    num_divisors(triangle)))