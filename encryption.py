import math

def encryption(s):
    # Write your code here

    # remove spaces
    s = s.replace(' ', '')

    # find bottom range of sqrt
    row = math.floor(math.sqrt(len(s)))

    # if square number, col = row
    if row**2 == len(s):
        col = row
    # else col is rounded up to row + 1
    else:
        col = row + 1

    # split the string into groups by their index modulo the col size
    ans = []
    for i, l in enumerate(s):
        group = i % col
        if group >= len(ans):
            ans.append(l)
        else:
            ans[group] += l

    # join list back together with spaces between
    ans = ' '.join(ans)

    return ans


print(encryption('have a nice day'))
print(encryption('feedthedog'))
print(encryption('ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'))