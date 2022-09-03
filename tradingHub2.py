def maxDifference(px):
    # Write your code here
    maxSpread = -1
    minPx = px[0]
    for i in range(1, len(px)):
        diff = px[i] - minPx
        if diff > maxSpread:
            maxSpread = diff
        if px[i] < minPx:
            minPx = px[i]
    if maxSpread == 0:
        maxSpread = -1
    
    return maxSpread


print(maxDifference([7, 9, 5, 6, 3, 2]))
print(maxDifference([11, 2, 3, 10, 2, 4, 8, 1]))