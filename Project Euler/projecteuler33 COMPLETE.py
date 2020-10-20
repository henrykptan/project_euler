'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''
def cancellation_test(a, b):
	A, B = str(a), str(b)	
	for i in range(0,2):
		for j in range(0,2):
			if A[i] == B[j]:
				if (int(A[(i+1)%2])/int(B[(j+1)%2])) == (a/b):
					return True
				else: 	
					continue
			else: 
				continue			

for d1 in range(1, 10):
	for d2 in range(1,10):
		if d1 == d2:
			break
		D = int(str(d1)+str(d2))
		for N in range(10,D):
			if cancellation_test(N, D):
				print(N, D, N/D)
				

				




	
	
	



