"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right
corner.

How many such routes are there through a 20×20 grid?
"""
import time


def routes(x, y, results_dict):
    """
    Number of routes from (a,b) to (0,0) in a grid (think of it as being reflected, so can move `left and down`)
    results_dict keys are the starting position - values are the number of routes to get to (0,0) ie dict<tuple, int>
    """
    if (x, y) in results_dict:  # if the value is already in the results cache then we don't need to calculate again
        return results_dict[(x, y)]

    # we only look at the top half of the grid
    # (as if you swap moves right/down you get equivalent number of paths)
    elif x > y:
        r = routes(y, x, results_dict)

    elif x == 0:
        return 1  # only one path when x coordinate is 0

    # from any one point you can either go down or left, then the sum of the positions gives the total for the original
    else:
        r = routes(x - 1, y, results_dict) + routes(x, y - 1, results_dict)
    results_dict[(x, y)] = r
    return r


if __name__ == '__main__':
    start = time.time()

    results = {}  # create a dictionary to keep track of the results:

    x_1, y_1 = 20, 20

    print("solution = {} found in {} seconds".format(routes(x_1, y_1, results), time.time() - start))
