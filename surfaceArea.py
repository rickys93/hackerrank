def surfaceArea(A):
    # Write your code here
    surfaceArea = 0
    zeroBoxes = []
    

    # make array of zeroes of length A[0]
    for r in A[0]:
        zeroBoxes.append(0)

    # insert the array of zeroes either end of A 
    # to make working the surface area out easier
    A.insert(0, zeroBoxes)
    A.append(zeroBoxes)


    for i in range(1, len(A)-1):

        # add the top and bottom of the current row
        surfaceArea += 2 * len(A[i])

        # add the sides of the blocks
        for n, box in enumerate(A[i]):
            # finding surface area between each box in the row
            if n == 0:
                surfaceArea += box

                # incase there's only one row
                if len(A[i]) == 1:
                    surfaceArea += box
                else:
                    surfaceArea += max(0, box - A[i][n + 1])
                
            elif n == len(A[i])-1:
                surfaceArea += max(0, box - A[i][n - 1])
                surfaceArea += box

            else:
                surfaceArea += max(0, box - A[i][n - 1])
                surfaceArea += max(0, box - A[i][n + 1])

            # finding surface area between the current box and the next row
            surfaceArea += max(0, box - A[i+1][n])
            surfaceArea += max(0, box - A[i-1][n])

    return surfaceArea








if __name__ == '__main__':
    f = open('./surfaceArea.txt', 'r')
    test = f.read()
    A = []

    for i in range(len(test.split('\n'))):
        A.append(list(map(int, test.split('\n')[i].split(' '))))
    # st = time.time()
    # print(surfaceArea(A))
    # et = time.time()

    # elapsedTime = et - st
    # print(elapsedTime)
    print(surfaceArea([[1],[2]]))

    # assert surfaceArea([[1, 3, 4],[2, 2, 3],[1, 2, 4]]) == 60
    assert surfaceArea([[1]]) == 6
    assert surfaceArea([[100, 93, 96, 92, 92, 98, 99, 100, 100, 96]]) == 2174

    # assert surfaceArea(A) == 705