"""
 Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

if __name__ == '__main__':

    current_num = 1  # the number in the spiral
    diag_sum = 1  # the sum of the diagonals
    square_side_length = 1  # the size of the square (size x size)
    while square_side_length < 1001:
        square_side_length += 2  # each new layer increases the size by 2
        for i in range(0, 4):  # for the four corners
            current_num += (square_side_length - 1)  # want to move size-1 spaces to get from corner to corner
            diag_sum += current_num

    print(diag_sum)
