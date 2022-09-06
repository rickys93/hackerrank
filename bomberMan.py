def bomberMan(n, grid):
    # Write your code here
    ans = []

    if n > 2 and n % 2 == 0:
        for row in grid:
            r = 'O' * len(row)
            ans.append(r)
        return ans
    else:
        bombsPlanted = {0:set()}
        for row, r in enumerate(grid):
            for col in range(len(r)):
                if grid[row][col] == 'O':
                    bombsPlanted[0].add((row,col))
        
        for i in range(1, n+1):
            bombsPlanted[i] = set()
            if i % 2 == 0:
                for row, r in enumerate(grid):
                    for col in range(len(r)):
                        plantBombAt(row, col, i, grid, bombsPlanted)
                        
            elif i >= 3 and i % 2 == 1:


                    explodeBombAt(row, col, i, grid, bombsPlanted)
                    

    return grid
                        
                                


def plantBombAt(row, col, i, grid, bombsPlanted):
    if grid[row][col] == '.':
        bombsPlanted[i].add((row,col))

        # changing . for O to indicate bomb placed
        grid[row] = grid[row][:col] + 'O' + grid[row][col+1:]

        return grid, bombsPlanted

def explodeBombAt(row, col, i, grid, bombsPlanted):
    bombsExploding = bombsPlanted[i-3]
    for row, col in bombsExploding:
        if grid[row][col] != 'O': return

        rows = len(grid)
        cols = len(grid[0])

        directions = ((0,1),(1,0),(0,-1),(-1,0))
        grid[row] = grid[row][:col] + '.' + grid[row][col+1:]
        for dx, dy in directions:
            cRow = row + dx
            cCol = col + dy
            if cRow <= rows - 1 and cRow >= 0 and cCol <= cols - 1 and cCol >= 0 and grid[cRow][cCol] == 'O' and (cRow,cCol) not in bombsExploding:
                grid[cRow] = grid[cRow][:cCol] + '.' + grid[cRow][cCol+1:]
                          

                

grid = [
    '...',
    '.O.',
    '...'
]
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


    








