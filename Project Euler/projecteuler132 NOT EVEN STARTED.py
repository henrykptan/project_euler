'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, 
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 186 * 39 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


two numbers length a and b -> product must be of length between max(a, b) and a+b

ie  max(a, b) <= p <= a + b 

given our list of numbers [1,2,3,4,5,6,7,8,9]

lengths a + b + c = 9, and fix a > b to avoid repetition

possible lengths: 
4, 1, 4  conditions: b != 1 
3, 3, 3
3, 2, 4

Brute force - try all permutations of 9 numbers 

'''
import time


def isPandigital(n):
	numString = str(n)
	size = len(numString)
	digits = [i for i in numString]
	for i in range(1, size+1):
		if str(i) not in digits:
			return False
	return True		

def isEquationAndPandigital(a, b, c):
	if (int(a)*int(b) != int(c)) :
		return False
	return (isPandigital(str(a) + str(b) + str(c)))

def swap(inputArray, aIndex, bIndex):
	temp = inputArray[aIndex]
	inputArray[aIndex] = inputArray[bIndex]
	inputArray[bIndex] = temp	
	return inputArray	

def permute(inputString, startIndex, endIndex, outputArray):
	stringArray = list(inputString)
	if (startIndex == endIndex):
		outputArray.append("".join(stringArray))
	else:
		for index in range(startIndex, endIndex+1):
			# swap the two elements in the array
			swap(stringArray, startIndex, index)
			permute("".join(stringArray), startIndex + 1, endIndex, outputArray)
			# swap the two elements back 
			swap(stringArray, startIndex, index)


if (__name__ == "__main__"):

	permutations = []
	permute(str(123456789), 0, 8, permutations)
	resultsNum = 0
	for perm in permutations:
		if isEquationAndPandigital(perm[0:4], perm[4], perm[5:9]):
			print(perm[0:4], perm[4], perm[5:9])
			resultsNum = resultsNum + 1
		elif isEquationAndPandigital(perm[0:3], perm[3:6], perm[6:9]):
			print(perm[0:3], perm[3:6], perm[6:9])
			resultsNum = resultsNum + 1
		elif isEquationAndPandigital(perm[0:3], perm[3:5], perm[5:9]):
			print(perm[0:3], perm[3:5], perm[5:9])
			resultsNum = resultsNum + 1

	print("found " + str(resultsNum) + " solutions")




#                                                          permute(123, 0, 2)
#                        permute(123, 1, 2)                permute(213, 1, 2)                permute (321, 1, 2)
#             permute(123, 2, 2) permute(132, 2, 2) permute(213, 2, 2) permute(231, 2, 2)  permute(321, 2, 2) permute(312, 2, 2)