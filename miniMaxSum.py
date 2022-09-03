def miniMaxSum(arr):
    # Write your code here
    minArr = arr.copy()
    minArr.remove(max(arr))
    minSum = sum(minArr)

    maxArr = arr.copy()
    maxArr.remove(min(arr))
    maxSum = sum(maxArr)

    print(minSum, maxSum)



arr1 = [1, 3, 5, 7, 9, 3, 65, 8, 43, 1, 4]
miniMaxSum(arr1)

