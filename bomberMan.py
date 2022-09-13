def bomberMan(n, grid):
    # Write your code here
    if n > 2 and n % 2 == 0:
        ans = []
        for row in grid:
            r = 'O' * len(row)
            ans.append(r)
        return ans
    else:
        ansDict = {}

        for i in range(0, 6):
            for row in range(len(grid)):
                for col in range(len(grid[0])):
         
                    if grid[row][col] == 'O':
                        turnRowColTo(row, col, grid, '3')
                    elif grid[row][col] == '3':
                        turnRowColTo(row, col, grid, '2')
                    elif grid[row][col] == '2':
                        turnRowColTo(row, col, grid, '1')
                    elif grid[row][col] == '1':
                        turnRowColTo(row, col, grid, '.')

                        explodeNeighbours(row, col, grid)
  
                    if i % 2 == 0 and i > 0:
                                if grid[row][col] == '.':
                                    turnRowColTo(row, col, grid, '3')

            
            ansDict[i] = turnBackToO(grid)

        if n < 3:
            ans = ansDict[n]
        else:
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