"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?

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


# def permute(input_string, start_index, end_index, output_array):
#     string_array = list(input_string)
#     if start_index == end_index:
#         output_array.append("".join(string_array))
#     else:
#         for index in range(start_index, end_index + 1):
#             # swap the two elements in the array
#             swap(string_array, start_index, index)
#             permute("".join(string_array), start_index + 1, end_index, output_array)
#             # swap the two elements back
#             swap(string_array, start_index, index)


if __name__ == "__main__":
    # len(a) = 4
    for i in range(10000):
        if is_nine_pandigital(str(i) + str(2 * i)):
            print("start at " + str(i), "n = " + str(2), "pandigital " + str(i) + str(2 * i))
    # len(a) = 3
    for i in range(1000):
        if is_nine_pandigital(str(i) + str(2 * i) + str(3 * i)):
            print("start at " + str(i), "n = " + str(3), "pandigital " + str(i) + str(2 * i) + str(3 * i))
    # len(a) = 2
    for i in range(100):
        if is_nine_pandigital(str(i) + str(2 * i) + str(3 * i) + str(4 * i)):
            print("start at " + str(i), "n = " + str(4), "pandigital " + str(i) + str(2 * i) + str(3 * i) + str(4 * i))
    # len(a) = 1
    for i in range(100):
        num_to_test = str(i)
        count = 2
        while len(num_to_test) < 9:
            num_to_test += str(count * i)
            count += 1
        if is_nine_pandigital(num_to_test):
            print("start at " + str(i), "pandigital " + num_to_test)
