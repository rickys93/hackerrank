from ctypes import sizeof


def connectedCell(matrix):
    visited = set()
    # Write your code here
    largestRegion = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and (row,col) not in visited:
                sizeOfRegion = calculateRegion(matrix, row, col, 1, visited)
                if sizeOfRegion > largestRegion:
                    largestRegion = sizeOfRegion

    return largestRegion


def calculateRegion(matrix, row, col, sizeOfRegion, visited):
    if (row,col) in visited:
        return 0

    visited.add((row,col))

    if matrix[row][col] == 0:
        return 0

    directions = ((1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,-1),(1,1),(-1,1))
    for dx, dy in directions:
        cRow = row + dx
        cCol = col + dy
        if cRow >= 0 and cRow <= len(matrix) - 1 and cCol >= 0 and cCol <= len(matrix[0]) - 1 and (cRow,cCol) not in visited and matrix[cRow][cCol] == 1:
            sizeOfRegion = calculateRegion(matrix, cRow, cCol, sizeOfRegion, visited) + 1

    return sizeOfRegion


grid = [
    [1, 1, 1, 0], 
    [0, 1, 1, 0], 
    [0, 0, 1, 0], 
    [1, 0, 0, 0]
    ]

print(connectedCell(grid))