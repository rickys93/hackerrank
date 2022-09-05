a = 'cded'
b = 'dcfc'

def makeAnagram(a, b):
    # Write your code here
    listA = []
    listB = []
    deleteCount = 0
    for l in a:
        if l not in listA:
            listA.append(l)
            lDiff = abs(a.count(l) - b.count(l))
            deleteCount += lDiff

    for l in b:
        if l not in listA and l not in listB:
            deleteCount += b.count(l)
            listB.append(l)


