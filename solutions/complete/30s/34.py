"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def factorial(num):
    if num == 0:
        return 1
    if num >= 1:
        return num * factorial(num - 1)


def factorial_sum(num):
    string_num = str(num)
    total = 0
    for i in range(0, len(string_num)):
        total += factorial(int(string_num[i]))
    return total


if __name__ == '__main__':

    total = 0
    for n in range(3, 1000000):
        if factorial_sum(n) == n:
            total += n
    print(total)
