"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def have_the_same_digits(a, b):
    string_a, string_b = str(a), str(b)
    nums = []
    for i in range(0, len(string_a)):
        nums.append(string_a[i])
    for j in range(0, len(string_b)):
        if string_b[j] not in nums:
            return False
        else:
            nums.remove(string_b[j])
    return not nums

if __name__ == '__main__':

    for n in range(1, 1000000):
        if have_the_same_digits(n, 2 * n) and have_the_same_digits(n, 3 * n) and have_the_same_digits(n, 4 * n) \
                and have_the_same_digits(n, 5 * n) and have_the_same_digits(n, 6 * n):
            print(n, 2 * n, 3 * n, 4 * n, 5 * n, 6 * n)
        else:
            continue
