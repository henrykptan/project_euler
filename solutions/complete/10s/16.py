"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


def digit_sum(x):
    result = 0
    while x > 0:
        result += x % 10
        x //= 10
    return result


print(digit_sum(2 ** 1000))
