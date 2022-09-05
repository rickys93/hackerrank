def formingMagicSquare(s):
    # Write your code here
    ans = 0


    # there are only a certain amount of combinations of magic square
    ans = 45

    # each position of the corners (the opposite corners have to be 6 and 4 or 8 and 2)
    pos = ((0,0), (2,0), (2,2), (0,2))
    
    # we are going to cycle through each possible combination of magic square and find the one that requires the least amount of changes
    for i in range(4):
        # create new square to keep track of the corner numbers
        newSquare = [[0,0,0],[0,0,0],[0,0,0]]

        # 5 is always in the middle 
        change = abs(s[1][1] - 5)

        # here was choose position 4 and position 6
        p4 = s[pos[i][0]][pos[i][1]]
        newSquare[pos[i][0]][pos[i][1]] = 4

        p6 = s[pos[(i + 2) % 4][0]][pos[(i + 2) % 4][1]]
        newSquare[pos[(i + 2) % 4][0]][pos[(i + 2) % 4][1]] = 6

        # we find the cost of changing these to te new numbers
        change += abs(p4 - 4)
        change += abs(p6 - 6)

        for x in [i+1,i+3]:
            # here was choose position 8 and position 2
            change2 = change
            p8 = s[pos[x % 4][0]][pos[x % 4][1]]
            newSquare[pos[x % 4][0]][pos[x % 4][1]] = 8
            p2 = s[pos[(x + 2) % 4][0]][pos[(x + 2) % 4][1]]
            newSquare[pos[(x + 2) % 4][0]][pos[(x + 2) % 4][1]] = 2

            # we find the cost of changing them to 8 and 2
            change2 += abs(p8 - 8)
            change2 += abs(p2 - 2)
            
            # here we find the cost of changing the rest of the numbers
            change2 += abs(s[0][1] - (15 - sum(newSquare[0])))
            change2 += abs(s[2][1] - (15 - sum(newSquare[2])))
            change2 += abs(s[1][0] - (15 - (newSquare[0][0] + newSquare[2][0])))
            change2 += abs(s[1][2] - (15 - (newSquare[0][2] + newSquare[2][2])))

            # if current combination is lowest, set as answer
            if change2 < ans:
                ans = change2
    
    return ans

        




sq = [
    [4, 8, 2], 
    [4, 5, 7], 
    [6, 1, 6]
]
print(formingMagicSquare(sq))

    


