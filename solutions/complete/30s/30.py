"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits
"""


def fifth_power_test(num):
    output = 0
    x = str(num)
    for digit in x:
        output += int(digit) ** 5
    return output == num


if __name__ == '__main__':

    ans = 0
    for n in range(2, 1000000):
        if fifth_power_test(n):
            ans += n
    print(ans)
