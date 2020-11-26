"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


# note - in order to fit all of the numbers in we need to multiply either size:
# 2 x 3 = 4
# 1 x 4 = 4 ONLY 


def is_pandigital(num):
    integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_string = str(num)
    for n in range(0, len(num_string)):
        if num_string[n] in integers:
            integers.remove(num_string[n])
    return not integers


if __name__ == '__main__':

    s = []
    for i in range(2, 99):
        if i < 10:
            start = 1234
        else:
            start = 123
        for j in range(start, 10000 // i):  # floor function is very smart, we don't like decimals
            if is_pandigital(str(i) + str(j) + str(i * j)):
                if i * j not in s:
                    s.append(i * j)

    ans = 0
    for i in range(0, len(s)):
        ans += s[i]
    print(ans)
