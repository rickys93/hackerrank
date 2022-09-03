import math
from pdb import lasti2lineno






def maxSubsetSum(arr):
    #first we should find all subsets 

    #create empty list for subsets
    lstAllSubsets = []
    lstNewSubsetss = []
    for i, n in enumerate(arr):
        if [n] not in lstAllSubsets:
            lstAllSubsets.append([n])
        newLstSubsets = []
        count = 0
        lstSlice = arr[i+2:]
        while count < len(lstSlice):
            subSet = [n, lstSlice[count]]
            lstNewSubsetss.append((subSet, count + i + 2))
            lstAllSubsets.append(subSet)
            count += 1


        while lstNewSubsetss:
            lstNewSubsetss = addOnNumbers(lstAllSubsets, lstNewSubsetss, arr)


    maxSubsetSum = 0
    for lst in lstAllSubsets:
        sumLst = sum(lst)
        if sumLst > maxSubsetSum:
            maxSubsetSum = sumLst

    return maxSubsetSum

    
def addOnNumbers(lstAllSubsets, lstSubsets, arr):
    lstNewSubsets = []
    for lst in lstSubsets:
        count = 0
        if lst[1]+2 < len(arr):
            lstSlice = arr[lst[1]+2:]
            while count < len(lstSlice):
                subSet = lst[0] + [lstSlice[count]]
                lstNewSubsets.append((subSet, count + lst[1] + 2))
                lstAllSubsets.append(subSet)
                count += 1 
    return lstNewSubsets
    


lst1 = [4, -2, 5, 9, 1, -2, 3, 20]
lst2 = [4, -2, 5, 9, 1, -2]
lst3 = [100, -2, 5, 9, 1, -2, 3, 20]
lst4 = [-7, -4, -1]
lst5 = []
lst6 = []
lst7 = []
lst8 = []        


print(maxSubsetSum(lst1))

assert maxSubsetSum(lst1) == 33
assert maxSubsetSum(lst2) == 13
assert maxSubsetSum(lst3) == 129
assert maxSubsetSum(lst4) == 0

