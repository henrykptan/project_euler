'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the SUM of all the amicable numbers under 10000.
'''
import time
start = time.time()

def divisorsum(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: 
            s += i
    return s

def amicable_pairs_xrange(n):
    '''
    We create a list of the sum of the divisors of each of the numbers in our range
    Then for each number we test if the divisorsum is 
    '''
    L = [divisorsum(i) for i in range(n + 1)]
    pairs = []
    for i in range(n + 1):
        ind = L[i]
        if i < ind and 0 <= ind and ind <= n and L[ind] == i:
            pairs.append([i,ind])
    return sum_pairs
 
def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])

print("Solution is {} found in time {}".format(sum_pairs(amicable_pairs_xrange(10000)), time.time()-start))

