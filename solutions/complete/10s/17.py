"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""
UNITS = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]  # number of letters for 0-20
TENS = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]  # number of letters for tens
HUNDREDS = 7

if __name__ == '__main__':

    total = 0

    for i in range(1, 1000):
        a = int(i % 10)  # gives units
        b = int((i % 100 - a) / 10)  # gives tens
        c = int((i - (b * 10 + a)) / 100)  # gives hundreds
        if c == 0:  # first for 1-99
            if (b * 10 + a) < 20:
                total += UNITS[int((b * 10 + a))]
            else:
                total += UNITS[a] + TENS[b]
        else:  # then for 100-999
            total += UNITS[c] + HUNDREDS
            if b == 0 and a == 0:
                continue
            else:
                total += 3  # "and"
                if (b * 10 + a) < 20:
                    total += UNITS[int((b * 10 + a))]
                else:
                    total += UNITS[a] + TENS[b]
    total += (3 + 8)  # "one thousand"

    print(total)
