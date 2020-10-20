'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right 
corner.

How many such routes are there through a 20×20 grid?
'''
import time 

start = time.time()

results = {} # create a DICTIONARY TO KEEPP TRACKKK of the results: keys are the starting position - values are the number of routes



def routes(a, b):
    """
    Number of routes from (a,b) to (0,0) in a grid
    """
    if (a, b) in results: # if the value is already in the results cache then we don't need to calculate again
        return results[(a, b)]
    elif a > b: 
        r = routes(b, a) # we only look at the top half of the grid (as if you swap moves right/down you get equivalent number of paths)
    elif a == 0:
        return(1) # only one path when you start at the end point 
    else:
        r = routes(a-1, b) + routes(a, b-1)  # from any one point you can either go down or left, then the sum of those positions gives the total for the original
    results[(a,b)] = r
    return(r)    

x, y = 20, 20        

print("solution = {} found in {} seconds".format(routes(x, y), time.time()-start))

# this is so much quicker because it keeps track of previous results, cutting down the number of computations (still recursive)

