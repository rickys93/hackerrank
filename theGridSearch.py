# https://www.hackerrank.com/challenges/the-grid-search/problem
# Given an array of strings of digits G, try to find the occurrence of a given pattern of digits P. 
#In the grid and pattern arrays, each string represents a row in the grid


from operator import index


def gridSearch(G, P):
    # assume that pattern is not in G
    patternInG = False

    for numRow, row in enumerate(G):
        # start at beginning of row
        indexPattern = 0

        # if first pattern is in current row and pattern not found yet
        # we need to make sure that we check each matching pattern in the row, not just the first one
        while P[0] in row[indexPattern:] and not patternInG:

            # we have found a match of the first row of P, now we assume pattern is in G until this current iteration is proved wrong 
            patternInG = True

            # find the index of the current pattern
            indexPattern += row[indexPattern:].index(P[0])

            # find out if the pattern is in each row below
            for i in range(1, len(P)):
                if indexPattern+len(P[i]) <= len(row):

                    # here we find the integers below the current row and see if they match
                    rowBelow = G[numRow+i][indexPattern:indexPattern+len(P[i])]
                    if P[i] == rowBelow:
                        continue
                    else:
                        # if one row of the pattern does not match, this current iteration does not match the pattern and we do our next search
                        patternInG = False
                        break
            indexPattern += 1

    return 'YES' if patternInG else 'NO'
                        

G = ['15967259','22452334','34967121']
P = ['59','34','22']

gridSearch(G, P)