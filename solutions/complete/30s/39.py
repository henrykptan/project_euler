"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def is_pythag_triple(a, b, c):
    if a ** 2 == b ** 2 + c ** 2:
        return True
    else:
        return False


if __name__ == '__main__':

    totals = [0] * 1000

    for i in range(1, 998):
        for j in range(1, i):
            for k in range(1, 1000 - (i + j)):
                if is_pythag_triple(i, j, k):
                    totals[i + j + k] += 1

    print(totals.index(max(totals)))
