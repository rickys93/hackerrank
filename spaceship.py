
def spaceship(g, f):
    # create a new array to place the lowest option to each star so far
    lstDistances = []
    # this is the start, so there's only one option
    lstDistances.append(g[0])

    for i in range(1, len(g)):
        # create new array for each row to place minimum distance to each star
        lstDistances.append([])
        currentRow = g[i]
        for n in range(len(currentRow)):
            # the first and last star must have come from the first and last star of the previous row respectively 
            # first star in row
            if n == 0:
                lstDistances[i].append(lstDistances[i-1][0] + currentRow[n])
            # last star in row
            elif n == len(currentRow) - 1:
                lstDistances[i].append(lstDistances[i-1][-1] + currentRow[n])
            # for all stars in the middle, there are only 2 options of which star to come from
            # by choosing the lowest of the running count from previous row, we will definitely have the lowest route to this particular star
            else:
                lstDistances[i].append(min(lstDistances[i-1][n-1] + currentRow[n], lstDistances[i-1][n] + currentRow[n]))

    # choose the minimum from the list of distances to each end star
    # if this is less than or equal to the fuel f, then it is possible
    if min(lstDistances[-1]) <= f:
        return 'Possible'

    # otherwise, not possible
    return 'Impossible'


g = [
    [15], 
    [2, 3],
    [6, 7, 9],
    [11, 2, 4, 10]
]

f = 20

print(spaceship(g, f))