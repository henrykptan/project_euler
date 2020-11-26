"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666...,
and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Notes

Let n < d, and you're trying to figure out the repeating part of n/d. Let p be the number of digits in the repeating
part:
then n/d = R * 10^(-p) + R * 10^(-2p) + ... = R * ((10^-p)^1 + (10^-p)^2 + ...).
The bracketed part is a geometric series, equal to 1/(10^p - 1).

So n / d = R / (10^p - 1).
Rearrange to get R = n * (10^p - 1) / d.
To find R, loop p from 1 to infinity, and stop as soon as d evenly divides n * (10^p - 1)

"""


def dec_cycle_len(numerator, denominator):  # where d>n
    x = numerator * (10 ^ 1 - 1)
    z = x
    power = 1
    while z % denominator:
        z = z * 10 + x
        power += 1
    return power


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    length = 1
    ans = 0
    for n in range(1, 1000):
        if is_prime(n):
            if dec_cycle_len(1, n) > ans:
                length = dec_cycle_len(1, n)
                ans = n
        else:
            continue

    print(ans)

