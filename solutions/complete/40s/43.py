"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


def is_nine_pandigital(n_string):
    if len(n_string) != 9:
        return False

    n_digits = [string_digit for string_digit in n_string]
    digit_list = [str(digit) for digit in range(1, 10)]
    for digit in digit_list:
        if digit not in n_digits:
            return False

    return True


def swap(input_array, a_index, b_index):
    temp = input_array[a_index]
    input_array[a_index] = input_array[b_index]
    input_array[b_index] = temp
    return input_array


def permute(input_string, start_index, end_index, output_array):
    string_array = list(input_string)
    if start_index == end_index:
        output_array.append("".join(string_array))
    else:
        for index in range(start_index, end_index + 1):
            # swap the two elements in the array
            swap(string_array, start_index, index)
            permute("".join(string_array), start_index + 1, end_index, output_array)
            # swap the two elements back
            swap(string_array, start_index, index)


if __name__ == "__main__":

    permutations = []
    permute(str(1234567890), 0, 9, permutations)

    sol = 0

    for perm in permutations:
        if int(perm[7:]) % 17 == 0 and int(perm[6:9]) % 13 == 0 and int(perm[5:8]) % 11 == 0 and \
                int(perm[4:7]) % 7 == 0 and int(perm[3:6]) % 5 == 0 and int(perm[2:5]) % 3 == 0 and \
                int(perm[1:4]) % 2 == 0:
            sol += int(perm)
    print(sol)
