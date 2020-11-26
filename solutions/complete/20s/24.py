"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import islice


def get_permutations(digits: list[str]) -> str:
    number_of_digits = len(digits)
    if number_of_digits <= 1:
        yield ''.join(digits)
    else:
        # for each digit, bring to front then add all perms of the remaining nums
        for index in range(number_of_digits):
            for permutation in get_permutations(digits[:index] + digits[index + 1:]):
                yield digits[index] + permutation


def get_nth_generator_value(iterable, n, default=None):
    return next(islice(iterable, n, None), default)


if __name__ == '__main__':
    perms_generator = get_permutations([str(num) for num in range(10)])
    print(get_nth_generator_value(perms_generator, 999999))
