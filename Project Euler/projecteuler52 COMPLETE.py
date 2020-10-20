'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def same_digits(a,b):    # creates an array containing all of the individual digits of the first number, then in turn removes the digits if they are in the
	A,B = str(a), str(b) # second number then tests if the array is empty
	nums = []
	for i in range(0, len(A)):
		nums.append(A[i])
	for j in range(0, len(B)):
		if B[j] not in nums:
			return False
		else:	
			nums.remove(B[j])
	if nums == []:
		return True
	else:
		return False	

for n in range(0,1000000):
	if same_digits(n, 2*n) and same_digits(n, 3*n) and same_digits(n, 4*n) and same_digits(n, 5*n) and same_digits(n, 6*n):
		print(n, 2*n, 3*n, 4*n, 5*n, 6*n)
	else: continue	

