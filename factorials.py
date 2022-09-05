def extraLongFactorials(n):
    # Write your code here
    ans = n
    for i in range(n-1, 0, -1):
        ans = ans * i

    return ans


print(extraLongFactorials(45))