

def sumList(arr):

    sum = sumNumbers(arr, 0)

    return sum


def sumNumbers(arr, i):
    if i == len(arr) - 1:
        return arr[i]

    return sumNumbers(arr, i+1) + arr[i]
    
    


arr = [1, 2, 3, 4, 5]
print(sumList(arr))


def factorial(int):
    if int == 1:
        return int
    else:
        return factorial(int-1) + int


print(factorial(10))


def fibonacciSequence(n):
    if n == 1 or n == 2:
        return n
    else:
        return fibonacciSequence(n-2) + fibonacciSequence(n-1)

print(fibonacciSequence(7))



def sumNonNegativeInteger(num, mod, div):
    if (num % mod) / div == 0:
        return 0
    else:
        
        return sumNonNegativeInteger(int(num - (num % mod)), mod * 10, div * 10) + int((num % mod) / div)


print(sumNonNegativeInteger(4557, 10, 1))



def sumSeries(n):
    if n <= 0:
        return 0
    else:
        return sumSeries(n-2) + n
    


print(sumSeries(9))



def aPowerB(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    else:
        return a * aPowerB(a, b-1)

print(aPowerB(3, 1))



