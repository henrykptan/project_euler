"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                return False
    return True


def is_truncatable_prime(num):
    if num < 10:
        return False
    string_num = str(num)
    # first: left to right truncatable
    for i in range(0, len(string_num)):
        if not is_prime(int(string_num[i:])):
            return False
    # then: right to left truncatable
    for j in range(1, len(string_num) + 1):
        if not is_prime(int(string_num[:j])):
            return False
    return True


if __name__ == '__main__':

    count = 0
    ans = 0
    for n in range(0, 10000):
        if is_truncatable_prime(n):
            print(n)
            count += 1
            ans += n

    print('The total sum is {x}'.format(x=ans))
