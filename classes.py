import math
from pdb import lasti2lineno



def maxSubsetSum(arr):
    dp = {} # key : max index of subarray, value = sum
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i-2]+num, dp[i-1], num, dp[i-2])

    return dp[len(arr)-1]


    


lst1 = [4, -2, 5, 9, 1, -2, 3, 20]
lst2 = [4, -2, 5, 9, 1, -2]
lst3 = [100, -2, 5, 9, 1, -2, 3, 20]
lst4 = [-7, -4, -1]
lst5 = [8006, -3505, -2450, -2399, -3423, 8968, -2026, -3762, 3229, 3390, -3828, 5507, -2903, -2470, -3401, 5498, 6049, 3255, -8092, -7729, -2931, 6551,8006, -3505, -2450, -2399, -3423, 8968, -2026, -3762, 3229, 3390, -3828, 5507, -2903, -2470, -3401, 5498, 6049, 3255, -8092, -7729, -2931, 6551]
lst6 = []
lst7 = []
lst8 = []        


print(maxSubsetSum(lst5))
print(maxSubsetSum2(lst5))

assert maxSubsetSum(lst1) == 33
assert maxSubsetSum(lst2) == 13
assert maxSubsetSum(lst3) == 129
# assert maxSubsetSum(lst4) == 0

