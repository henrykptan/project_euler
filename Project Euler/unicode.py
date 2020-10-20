alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

def alphabet_combos(n): 
	'''
	wayyyy more confusing than you would think 
	- need to define recursively
	'''
	combos = []
	if n == 1:
		combos = alphabet
	else:
		for combo in alphabet_combos(n-1):
			for letter in alphabet:
				combos.append(combo + letter)
	return(combos)

'''
UNICODE
Each single character in a string can be represented by a number in UNICODE
We use ord() to get the code and ch() to get back to the character 
'''

			