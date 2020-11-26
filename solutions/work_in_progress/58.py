'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers 
lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, 
what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

# need to consider at what sequence the digits fall on the diagonals ie if we take the square edge length as a count n-
# We start at 1
# We move one step to the right 
# Then one step up we add to r
# Two steps across we add to l
# Two steps down we add to l
# Two steps right we add to r

# Generally:
# We start at middle value on the right
# One step outwards
# floor(n/2) up we add to r
# n-1 left...n-1 down...n-1 right
# 
import time

start = time.time()

right_diagonal = [1, 3, 7]  # create lists in order to append the diagonals' values
left_diagonal = [1, 5, 9]

square_length = 10  # the side length of the grd of numbers, can only be an odd number
v = 9  # our initial value, we count up as we go
l = 5  # starting by adding the layer of 5x5
while l < square_length:
    v += 1 + (l - 2)
    right_diagonal.append(v)
    v += (l - 1)
    left_diagonal.append(v)
    v += (l - 1)
    right_diagonal.append(v)
    v += (l - 1)
    left_diagonal.append(v)
    l += 2

diagonals = left_diagonal + right_diagonal


# We need to calculate whether each number is prime - we produce a list of prime up to the value square_length^2 SIEVE

def sieve(n):
    is_prime = [True] * n  # create an list of n trues
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated (when we generate)
    for i in range(3, int(n ** 0.5 + 1), 2):  # so we check the odds
        index = i * 2
        while index < n:  # we now go through every odd number up to sqrt(n)+1, and remove its multiples
            is_prime[index] = False
            index = index + i
    primes = [2]
    for i in range(3, n, 2):  # we then generate our set of primes (note no need to check evens after 2)
        if is_prime[i]:
            primes.append(i)
    return primes


primes = sieve(square_length ** 2)

prime_count = 0
for num in diagonals:  # We test whether each diagonal is prime
    if num in primes:
        prime_count += 1
        print(num)

print(diagonals)
print(prime_count)
print(primes)

print("Completed in {}".format(time.time() - start))
