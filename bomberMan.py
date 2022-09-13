#Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

#Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell , any valid cells  and  are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

#Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

#Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
#After one second, Bomberman does nothing.
#After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
#After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
#Bomberman then repeats steps 3 and 4 indefinitely.
#Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

#Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after  seconds.

def bomberMan(n, grid):

    # if n is even, always grid full of bombs
    if n > 2 and n % 2 == 0:
        ans = []
        for row in grid:
            r = 'O' * len(row)
            ans.append(r)
        return ans
    else:
        # store answers in dict
        ansDict = {}

        # when n = 3, 7, 11... grid is always the same
        # when n = 5, 9, 13... grid is also always the same 
        # so we only need to find the first 5 states of the grid
        for i in range(0, 6):
            for row in range(len(grid)):
                for col in range(len(grid[0])):
         
                    # extra seconds passed, update the grid
                    if grid[row][col] == 'O':
                        turnRowColTo(row, col, grid, '3')
                    elif grid[row][col] == '3':
                        turnRowColTo(row, col, grid, '2')
                    elif grid[row][col] == '2':
                        turnRowColTo(row, col, grid, '1')
                    # when bomb has 0 second left, explode them
                    elif grid[row][col] == '1':
                        turnRowColTo(row, col, grid, '.')

                        explodeNeighbours(row, col, grid)
  
                    if i % 2 == 0 and i > 0:
                                if grid[row][col] == '.':
                                    turnRowColTo(row, col, grid, '3')

            # store grid in correct format
            ansDict[i] = turnBackToO(grid)

        if n < 3:
            ans = ansDict[n]
        else:
            # if n = 3, 7, 11... or n = 5, 9, 13... use n = 3 or 5
            if n % 4 == 3:
                n = 3
            elif n % 4 == 1:
                n = 5
            ans = ansDict[n]
            
    return ans
                


def explodeNeighbours(row, col, grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = ((0,1),(1,0),(0,-1),(-1,0))


    for dx, dy in directions:
        cRow = row + dx
        cCol = col + dy
        if cRow <= rows - 1 and cRow >= 0 and cCol <= cols - 1 and cCol >= 0 and grid[cRow][cCol] != '1':
            turnRowColTo(cRow, cCol, grid, '.')


def turnRowColTo(row, col, grid, char):
    grid[row] = grid[row][:col] + char + grid[row][col+1:]


def turnBackToO(grid):
    newGrid = grid[:]
    for row in range(len(newGrid)):
        for col in range(len(newGrid[0])):
            if newGrid[row][col] != '.':
                turnRowColTo(row, col, newGrid, 'O')
    return newGrid