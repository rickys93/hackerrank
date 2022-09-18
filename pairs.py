import time

def pairs(k, arr):
    set1 = set(arr)
    set2 = [value + k for value in arr]
    return len(set1.intersection(set2))



# arr = [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254, 879792181, 1069262793]
# pairs(1, arr)


if __name__ == '__main__':
    f = open('./pairs.txt', 'r')
    test = f.read()

    k = int(test.split('\n')[0].split(' ')[1])

    arr = list(map(int, test.split('\n')[1].split(' ')))

    st = time.time()
    print(pairs(k, arr))
    et = time.time()

    elapsedTime = et - st
    print(elapsedTime)