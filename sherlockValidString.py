

def isValid(s):
    # Write your code here
    maxDict = {}

    #find the max and min count of letters in the string
    for l in s:
        if l not in maxDict:
            lCount = s.count(l) 
            maxDict[l] = lCount

    maxCount = max(list(maxDict.values()))
    minCount = min(list(maxDict.values()))
    numMaxValues = list(maxDict.values()).count(maxCount)
    # if there is only one letter with max letter count and all the other letter counts are 1 less
    if numMaxValues == 1 and maxCount == minCount + 1:
        return 'YES'
    #when only one letter in string
    elif len(maxDict) == 1:
        return 'YES'
    #when each letter appears the same amount of times
    elif maxCount == minCount and len(maxDict) * maxCount == len(s):
        return 'YES'
    else:
        numMinValues = list(maxDict.values()).count(minCount)
        dictLen = len(list(maxDict.values()))
        if numMinValues == 1 and minCount == 1 and numMaxValues + numMinValues == len(list(maxDict.values())):
            return 'YES'
        
    return 'NO'

assert isValid('xxxaabbccrry') == 'NO'
assert isValid('aabbccdde') == 'YES'
assert isValid('abcdde') == 'YES'
assert isValid('aabbc') == 'YES'
assert isValid('abcddeeff') == 'NO'
assert isValid('abcdee') == 'YES'
assert isValid('aaaaaa') == 'YES'
assert isValid('aaaabbb') == 'YES'
assert isValid('aaaabbbccc') == 'YES'
assert isValid('abcdefg') == 'YES'
assert isValid('aabbccddeeffgg') == 'YES'
assert isValid('aaabbbcccdddeeefffgg') == 'NO'
assert isValid('aaabbbcccdddeeefffgggg') == 'YES'
assert isValid('aaabbbcccdddeeefffggg') == 'YES'
assert isValid('abcdeefffff') == 'NO'
assert isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd') == 'YES'