"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.

NOTES:
- Solution > 56003
- When testing the substitutions, once we reach 3 that aren't prime then we stop
- Which numbers to swap out:
    - Not the last (since evens won't be prime)
    - Has to be a 0, 1 or 2


PLAN
- Work through the primes
- For each, test swapping out 1 number
- If there are multiple matching digits, then test
"""


def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime_list = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime_list.append(i)
    return prime_list


def replace_digits_in_int(test_prime, indices, num_to_sub_in):
    test_prime_array = [digit for digit in str(test_prime)]
    for index in indices:
        test_prime_array[index] = str(num_to_sub_in)
    return int(''.join(test_prime_array))


def get_matching_digits_indices_in_number(num):
    # Note removing if the index is the end
    # And only testing for 0, 1 or 2
    digit_list = [int(digit_string) for digit_string in str(num)]
    matching_indices = []
    for digit in range(3):
        if digit_list.count(digit) > 0:
            matching_indices.append([index for index in range(len(digit_list)) if digit_list[index] == digit])
    return filter(lambda index_list: len(digit_list) not in index_list, matching_indices)


def get_prime_number_family_value(test_prime, indices, prime_list):
    return sum(replace_digits_in_int(test_prime, indices, num) in prime_list for num in range(10))


if __name__ == "__main__":
    prime_list = sieve(999999)

    primes_not_to_test_again = []

    for prime in prime_list:
        if prime in primes_not_to_test_again:
            continue
        else:
            for indices in get_matching_digits_indices_in_number(prime):
                tested_primes = []
                prime_value_family_size = 0
                number_not_prime = 0
                for num_to_sub_in in range(10):
                    number_to_test = replace_digits_in_int(prime, indices, num_to_sub_in)
                    if number_to_test in prime_list:
                        tested_primes.append(number_to_test)
                        prime_value_family_size += 1
                    else:
                        number_not_prime += 1
                        if number_not_prime >= 2:
                            break
                if prime_value_family_size >= 7:
                    primes_not_to_test_again.extend(tested_primes)
                    print(prime, indices, prime_value_family_size)
