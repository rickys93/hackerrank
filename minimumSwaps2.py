# Complete the minimumSwaps function below.
arr = [7, 1, 3, 2, 4, 5, 6]
arr1 = [1, 7, 3, 6, 4, 5, 2]
arr2 = [4, 3, 1, 2]
arr3 = [1, 2, 3, 4]
arr4 = [4, 2, 3, 1]
arr5 = [4, 3, 2, 1]
arr6 = [4, 1, 2, 3]
arr7 = [3, 2, 12, 11, 9, 1, 4, 5, 7, 10, 8, 6]

def minimumSwaps(arr):
    indexesDone = []
    swapsDone = 0
    lastSwap = False
    for i, num in enumerate(arr, start=1):
        if i not in indexesDone:
            if num == i:
                indexesDone.append(i)
                continue
            elif i == arr[num-1]:
                indexesDone.append(i)
                indexesDone.append(num)
                swapsDone += 1
            else:
                lastSwap = True
                indexesDone.append(i)
                swapsDone += 1
    if lastSwap:
        swapsDone -= 1
    return swapsDone

print(minimumSwaps(arr7))