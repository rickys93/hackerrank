def almostSorted(arr):
    # add all index where the integer is less than previous integer
    lstDips = []
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            lstDips.append(i)
    
    # find the first and last num index from the list
    # these are the indexes of the integers of the answer if it's possible
    if lstDips:
        iFirstNum = lstDips[0] - 1
        iLastNum = lstDips[-1]

    # here we may require a swap, if the integers fit
    if len(lstDips) == 2:
        # this makes sure the integers fit when they are swapped
        if firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
            print('yes')
            print('swap ' + str(iFirstNum + 1) + ' ' + str(iLastNum + 1))
            return

    # here we may require a swap (the integers in question are next to each other)
    elif len(lstDips) == 1:
        if firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
            print('yes')
            print('swap ' + str(iFirstNum + 1) + ' ' + str(iLastNum + 1))
            return

    # here we have more than 2 integers not in order so the only way is to reverse the order
    elif len(lstDips) > 2:
        # if the integers are in reverse order
        if iFirstNum + len(lstDips) == iLastNum:
            if firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
                print('yes')
                print('reverse ' + str(iFirstNum + 1) + ' ' + str(iLastNum + 1))
                return

    # if no integers were less than previous i, must be in order already
    elif len(lstDips) == 0:
        print('yes')
        return

    # if made it this far, no option except it's not possible
    print('no')
    return

        

def firstLastNumsFit(lstDips, arr, iFirstNum, iLastNum):
    firstNum = arr[iFirstNum]
    lastNum = arr[iLastNum]

    # if the indexes are not at the ends of the array
    if iFirstNum > 0 and iLastNum < len(arr) - 1:
        # make sure the numbers can be swapped and be in order
        return firstNum <= arr[iLastNum + 1] and firstNum >= arr[iLastNum - 1] and lastNum >= arr[iFirstNum - 1] and lastNum <= arr[iFirstNum + 1]

    # are both at end of array
    elif iFirstNum == 0 and iLastNum == len(arr) - 1:
        return firstNum >= arr[iLastNum - 1] and lastNum <= arr[iFirstNum + 1]
 
    # firstNum is at beginning of array
    elif iFirstNum == 0:
        return firstNum <= arr[iLastNum + 1] and firstNum >= arr[iLastNum - 1] and lastNum <= arr[iFirstNum + 1]

    #lastNum is at end of array
    else:
        return firstNum >= arr[iLastNum - 1] and lastNum >= arr[iFirstNum - 1] and lastNum <= arr[iFirstNum + 1]


        







# almostSorted([4,2])
# almostSorted([3,1,2])
# almostSorted([1,5,4,3,2,6])
# almostSorted([2,3,11,6,8,4,12])
# almostSorted([2,3,7,6,8,9])
# almostSorted([2,3,7,6,8,9,4])
# almostSorted([2,3,7,6,5,9,10])
# almostSorted([2,3,7,6,5,9,10,4])
# almostSorted([1,2,4,5,7,8])