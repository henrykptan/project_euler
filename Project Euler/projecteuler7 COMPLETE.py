'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import time
from math import sqrt
start = time.time()
'''
def isPrime(n):
    if n < 2: return "lol" # not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False #also not prime
    return True #yay

def nthPrime(n):
    numberOfPrimes = 2
    prime = 3
    while numberOfPrimes < n:
        prime += 2
        if isPrime(prime):
            numberOfPrimes += 1
    return prime

print("ans is {}, found in time {}".format(nthPrime(10001), time.time()-start))
'''

def seive(n):
    primetf = [True]*n
    primetf[0] = False
    primetf[1] = False
    primetf[2] = True 
    for i in range(3, int(sqrt(n)+1), 2):
        index = 2*i
        while index < n:
            primetf[index] = False
            index += i
    primelist = [2]
    for i in range(3, n, 2):
        if primetf[i]:
            primelist.append(i)
    return primelist

# we want to take a guess as to how large the 10,001st prime is - we can use the Gaussian (?) prediction, ie log
