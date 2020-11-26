"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
if __name__ == '__main__':

    # Brute force
    # combinations = 1  # one £2 coin
    # combinations += 7  # for each combination of just 1 type of coin (aside from £2)
    # for a in range(0, 2):
    #     for b in range(0, 4):
    #         for c in range(0, 10):
    #             for d in range(0, 20):
    #                 for e in range(0, 40):
    #                     for f in range(0, 100):
    #                         for g in range(0, 200):
    #                             if 100 * a + 50 * b + 20 * c + 10 * d + 5 * e + 2 * f + g == 200:
    #                                 combinations += 1
    # print(combinations)

    # Smarter way - idea:
    # Iterative:
    # Starting with there being 1 possible way to get 0p
    # Start with 1p -
    # the number of ways to make 1p
    # = number of ways to make (1p - 1p)
    # = number of ways to make 0p
    # = 1
    # the number of ways to make 2p
    # = number of ways to make (2p - 1p)
    # = number of ways to make 1p
    # = 1
    # etc
    # Then add 2p
    # Starting from value of 2p, we follow the same pattern
    # etc etc

    target_value_in_pennies = 200
    coin_values_in_pennies = {1, 2, 5, 10, 20, 50, 100, 200}
    number_of_ways = [0] * (target_value_in_pennies + 1)
    number_of_ways[0] = 1
    for coin_value in coin_values_in_pennies:
        for value in range(coin_value, target_value_in_pennies+1):
            number_of_ways[value] += number_of_ways[value - coin_value]

    print(number_of_ways[target_value_in_pennies])