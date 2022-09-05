def pickingNumbers(a):
    # Write your code here
    ans = 0

    # to add already counted combos
    counted = set()
    for num in a:

        # try going 1 up or 1 down from current number and find the longest combo
        if (num, num+1) not in counted:
            newCount = a.count(num) + a.count(num+1)
            counted.add((num, num+1))

            if newCount > ans:
                ans = newCount

        if (num-1, num) not in counted:
            newCount = a.count(num-1) + a.count(num)
            counted.add((num-1, num))

            if newCount > ans:
                ans = newCount

    return ans


print(pickingNumbers([4, 6, 5, 3, 3, 1]))
print(pickingNumbers([1, 2, 2, 3, 1, 2]))
print(pickingNumbers([1, 2, 3, 3, 4, 5]))
print(pickingNumbers([2, 2]))