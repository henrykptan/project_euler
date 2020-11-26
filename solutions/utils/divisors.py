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