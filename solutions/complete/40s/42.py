"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall
call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

words = open("../../resources/words.txt").read().split(',')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def calculate_word_value(word):
    value = 0
    for letter in word:
        if letter in alphabet:
            value += int(alphabet.index(letter)) + 1
    return value


def get_triangle_numbers_up_to_n(n):
    nums = []
    c = 0
    while int((c / 2) * (c + 1)) <= n:
        nums.append(int((c / 2) * (c + 1)))
        c += 1
    return nums


if __name__ == '__main__':

    tri = get_triangle_numbers_up_to_n(15 * 26)

    total = 0
    count = 0
    for i in range(0, len(words)):
        word_total = 0
        word_total += calculate_word_value(words[i])
        if word_total in tri:
            total += word_total
            count += 1
        else:
            continue

    print(total)
    print(count)
