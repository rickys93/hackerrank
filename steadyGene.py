

from cgitb import small


def steadyGene(gene):
    # Write your code here
    emptyGeneCount = {
        'A':0,
        'C':0,
        'G':0,
        'T':0
    }

    genesToChange = emptyGeneCount.copy()
    geneCount = emptyGeneCount.copy()

    averageGenes = int(len(gene) / 4)
    for l in gene:
        geneCount[l] += 1

    for l in geneCount:
        genesToChange[l] = max(0, geneCount[l] - averageGenes)

    subString = ''
    for l in genesToChange:
        subString += l * genesToChange[l]

    return findSubString(gene, subString)
        

    # now we need to find the smallest substring containing the positive letters in genesToChange
    # smallestGuess = sum(genesToChange.values()) - 1
    # substringFound = False
    # while not substringFound:
    #     smallestGuess += 1
    #     for i in range(smallestGuess, len(gene)):
    #         subStringCount = emptyGeneCount.copy()
    #         substring = gene[i-smallestGuess:i]
    #         for l in substring:
    #             subStringCount[l] += 1

    #         substringFound = True
    #         for l in genesToChange:
    #             if genesToChange[l] > subStringCount[l] and genesToChange[l] > 0:
    #                 substringFound = False

    #         if substringFound:
    #             break


    # return smallestGuess


def findSubString(string, pat):
    no_of_chars = 256
 
    len1 = len(string)
    len2 = len(pat)
 
    # Check if string's length is
    # less than pattern's
    # length. If yes then no such
    # window can exist
    if len1 < len2:
 
        print("No such window exists")
        return ""
 
    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars
 
    # Store occurrence ofs characters of pattern
    for i in range(0, len2):
        hash_pat[ord(pat[i])] += 1
 
    start, start_index, min_len = 0, -1, float('inf')
 
    # Start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):
 
        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1
 
        # If string's char matches with
        # pattern's char then increment count
        if (hash_str[ord(string[j])] <= hash_pat[ord(string[j])]):
            count += 1
 

        # if all the characters are matched
        if count == len2:
 
            # Try to minimize the window
            a = ord(string[start])
            while (hash_str[ord(string[start])] > hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0):

                if (hash_str[ord(string[start])] > hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1
 
            # update window size
            len_window = j - start + 1
            if min_len > len_window:
 
                min_len = len_window
                start_index = start
 
    # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""
 
    # Return substring starting from
    # start_index and length min_len
    return min_len

        
        





gene = 'ACTGAAAGCCCCAGGTAAGGGCAA'

steadyGene(gene)