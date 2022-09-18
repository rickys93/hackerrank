def spaceship(g, f):

    if hasEnoughFuel(g, f, 0, 0):
        return 'Possible'
    
    return 'Impossible'


def hasEnoughFuel(g, f, i, n):

    fuelCount = fuelCount - g[i][n]

    if fuelCount < 0:
        return False
    if i == len(g) - 1:
        return True
    
    if hasEnoughFuel(g, fuelCount, i+1, n) or hasEnoughFuel(g, fuelCount, i+1, n+1):
        return True



g = [
    [13], 
    [2, 3],
    [1, 2, 9],
    [10, 2, 4, 10]
]

f = 20

print(spaceship(g, f))