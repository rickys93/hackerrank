# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
# If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. 
# The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
# Given the number of trailing days  and a client's total daily expenditures for a period of  days, determine the number of times the client will receive a notification over all  days.

import time
import bisect
from inspect import trace


def activityNotifications(expenditure, d):
    # if num of trailing days is greater than total amount of days, we always return 0
    if d >= len(expenditure): return 0

    
    countNotices = 0

    # grab the first lot of trailing days and sort into ascending order to find median
    trailingDays = expenditure[:d]
    trailingDays.sort()

    for i in range(d, len(expenditure)):        
        # now we compare the current day expenditure to 2 x median of d trailing days
        if d % 2 == 0:
            firstNum = int((d/2)-1)
            secondNum = firstNum + 1
            medianExp = trailingDays[firstNum] + trailingDays[secondNum]
            if expToAdd >= medianExp:
                countNotices += 1
        else:
            medianExp = trailingDays[int((d-1)/2)]
            if expToAdd >= medianExp * 2:
                countNotices += 1

        # this is element we want to remove and add on next run
        expToRemove = expenditure[i-d]
        expToAdd = expenditure[i]

        # bisect is a quick method to finding the indexes to remove and place the new element
        indexToRemove = bisect.bisect_left(trailingDays, expToRemove)
        trailingDays.pop(indexToRemove)

        indexToAdd = bisect.bisect(trailingDays, expToAdd)
        trailingDays.insert(indexToAdd, expToAdd)
       

    return countNotices


    

if __name__ == '__main__':
    f = open('./fraudulentActivity.txt', 'r')
    test = f.read()
    d = int(test.split('\n')[0].split(' ')[1])

    expenditure = list(map(int, test.split('\n')[1].split(' ')))
    st = time.time()
    print(activityNotifications(expenditure, d))
    et = time.time()

    elapsedTime = et - st
    print(elapsedTime)

# print(activityNotifications([2,3,4,2,3,6,8,4,5], 4))