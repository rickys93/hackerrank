from binascii import crc32


def jumpingOnClouds(c):
    # Write your code here
    countJumps = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c):
            if c[i+2] == 0:
                i += 2
            else:
                i += 1
        elif i + 1 < len(c):
            i += 1
        countJumps += 1


    return countJumps


c1 = [0, 0, 0, 1, 0, 0]
c2 = [0, 1, 0, 0, 0, 1, 0]
c3 = [0, 0, 1, 0, 0, 1, 0]
c4 = [0, 0, 0, 1, 0, 1, 0, 0]

print(jumpingOnClouds(c1))
assert jumpingOnClouds(c1) == 3
assert jumpingOnClouds(c2) == 3
assert jumpingOnClouds(c3) == 4
assert jumpingOnClouds(c4) == 4