alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

def alphabet_combos(n): 
	combos = []
	if n == 1:
		combos = alphabet
	else:
		for combo in alphabet_combos(n-1):
			for letter in alphabet:
				combos.append(combo + letter)
	return(combos)
print(alphabet_combos(2))
					