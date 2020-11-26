"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(x):
    sum1 = 0
    for i in range(1, x + 1):
        sum1 += (i * i)
    return sum1


def square_of_sum(y):
    sum2 = 0
    for i in range(1, y + 1):
        sum2 += i
    return sum2 * sum2


if __name__ == '__main__':
    print(abs(square_of_sum(100) - sum_of_squares(100)))
