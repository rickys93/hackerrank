def almostSorted(arr):
    lstDips = []
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            lstDips.append(i)
    
    if lstDips:
        iFirstNum = lstDips[0] - 1
        iLastNum = lstDips[-1]

    if len(lstDips) == 2:
        if firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
            print('yes')
            print('swap ' + str(iFirstNum + 1) + ' ' + str(iLastNum + 1))
            return

    elif len(lstDips) == 1:
        if firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
            print('yes')
            print('swap ' + str(iFirstNum + 1) + ' ' + str(iLastNum + 1))
            return

    elif len(lstDips) > 2:
        if iFirstNum + len(lstDips) == iLastNum:
            if firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
                print('yes')
                print('reverse ' + str(iFirstNum + 1) + ' ' + str(iLastNum + 1))
                return

    elif len(lstDips) == 0:
        print('yes')
        return

    
    print('no')
    return

        

def firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
    firstNum = arr[iFirstNum]
    lastNum = arr[iLastNum]

    # if the indexes are not at the ends of the array
    if iFirstNum > 0 and iLastNum < len(arr) - 1:
        # make sure the numbers can be swapped and be in order
        return firstNum <= arr[iLastNum + 1] and firstNum >= arr[iLastNum - 1] and lastNum >= arr[iFirstNum - 1] and lastNum <= arr[iFirstNum + 1]

    elif iFirstNum == 0 and iLastNum == len(arr) - 1:
        return firstNum >= arr[iLastNum - 1] and lastNum <= arr[iFirstNum + 1]
 
    elif iFirstNum == 0:
        return firstNum <= arr[iLastNum + 1] and firstNum >= arr[iLastNum - 1] and lastNum <= arr[iFirstNum + 1]

    else:
        return firstNum >= arr[iLastNum - 1] and lastNum >= arr[iFirstNum - 1] and lastNum <= arr[iFirstNum + 1]


        







almostSorted([4,2])
# almostSorted([3,1,2])
almostSorted([1,5,4,3,2,6])
almostSorted([2,3,11,6,8,4,12])
almostSorted([2,3,7,6,8,9])
almostSorted([2,3,7,6,8,9,4])
almostSorted([2,3,7,6,5,9,10])
almostSorted([2,3,7,6,5,9,10,4])
almostSorted([1,2,4,5,7,8])