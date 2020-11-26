"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def highest_power_of_2_in_num(num):
    i = 1
    while num / (2 ** i) >= 1:
        i += 1
    return i - 1


def convert_to_binary(num):
    digits = []
    total = num
    for i in range(0, highest_power_of_2_in_num(num) + 1):
        power_i = (highest_power_of_2_in_num(num) - i)  # to go in order of power increasing
        digits.append(str(int(total / (2 ** power_i))))  # int used as a floor function, adding the value to the array
        total -= (2 ** power_i) * int(
            total / (2 ** power_i))  # remaining total after minusing the contribution from 2^(power_i)
    return "".join(digits)


def is_palindrome_in_base_10_and_base_2(num):
    string_num = str(num)
    return string_num == string_num[::-1] and str(convert_to_binary(num)) == str(convert_to_binary(num))[::-1]


if __name__ == '__main__':

    ans = 0
    for n in range(0, 1000000):
        if is_palindrome_in_base_10_and_base_2(n):
            print(n, convert_to_binary(n))
            ans += n
    print(ans)
