def bomberMan(n, grid):
    # Write your code here
    ans = []

    if n > 2 and n % 2 == 0:
        for row in grid:
            r = 'O' * len(row)
            ans.append(r)
        return ans
    else:
        bombsPlanted = {0:grid}
        # bombsExploded = {1:set()}
        # for row, r in enumerate(grid):
        #     for col in range(len(r)):
        #         if grid[row][col] == 'O':
        #             bombsPlanted[0].add((row,col))
        standardGrid = []

        for row in range(len(grid)):
            standardGrid.append('.' * len(grid[0]))


    
        
        for i in range(1, n+1):
            
            if i % 2 == 0:
                bombsPlanted[i] = standardGrid.copy()
                for row, r in enumerate(grid):
                    for col in range(len(r)):
                        plantBombAt(row, col, i, grid, bombsPlanted)
                        
            elif i >= 3 and i % 2 == 1:
                explodeBombs(i, grid, bombsPlanted)
                    

    return grid
                        
                                


def plantBombAt(row, col, i, grid, bombsPlanted):
    if grid[row][col] == '.':
        # bombsPlanted[i].add((row,col))
        bombsPlanted[i][row] = bombsPlanted[i][row][:col] + 'O' + bombsPlanted[i][row][col+1:]

        # changing . for O to indicate bomb placed
        grid[row] = grid[row][:col] + 'O' + grid[row][col+1:]


def explodeBombs(i, grid, bombsPlanted):
    bombsExploding = bombsPlanted[i-3]

    for row in range(len(bombsExploding)):
        for col in range(len(bombsExploding[0])):
            if bombsExploding[row][col] == 'O' and grid[row][col] == 'O':
    # for row, col in bombsExploding:
    #     if grid[row][col] != 'O': continue

                explodeBombAt(i, row, col, bombsPlanted)

                rows = len(grid)
                cols = len(grid[0])

                directions = ((0,1),(1,0),(0,-1),(-1,0))

                for dx, dy in directions:
                    cRow = row + dx
                    cCol = col + dy
                    if cRow <= rows - 1 and cRow >= 0 and cCol <= cols - 1 and cCol >= 0 and grid[cRow][cCol] == 'O' and (cRow,cCol) not in bombsExploding:
                        explodeBombAt(i, cRow, cCol, bombsPlanted)


                          

def explodeBombAt(i, row, col, bombsPlanted):      
    grid[row] = grid[row][:col] + '.' + grid[row][col+1:]
    bombsPlanted[i-1] = bombsPlanted[i-1][row][:col] + '.' + bombsPlanted[i-1][row][col+1:]
    # if (row, col) in bombsPlanted[i-1]:
    #     bombsPlanted[i-1].remove((row, col))     

# grid = [
#     '.O..',
#     'O...',
#     '...O',
#     '....'
# ]
# grid =[
#     '.......', 
#     '...O...', 
#     '....O..',
#     '.......', 
#     'OO.....', 
#     'OO.....'
#     ]

grid = [
'.......',
'...O.O.',
'....O..',
'..O....',
'OO...OO',
'OO.O...']

bomberMan(5, grid)


    








