'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins? 
'''

combinations = 1 # one £2 coin 
combinations += 7 # for each combination of just 1 type of coin (aside from £2)
for a in range(0, 2):
	for b in range(0, 4):
		for c in range(0, 10):
			for d in range(0, 20):
				for e in range(0, 40):	
					for f in range(0, 100):
						for g in range(0, 200):
							if (100*a+50*b+20*c+10*d+5*e+2*f+g==200):
								print(a,b,c,d,e,f,g)
								combinations+=1
print(combinations)								
# this is very brute force-y, clunky and takes a frickin age to run - (ways to speed up????)



