import math


def isSquare(number):
    h = int(math.sqrt(number))
    if h**2 == number:
        return True
    return False


def newChecker(n,m):
    a = 36 * ((m ** 2) + (n ** 2)) - (12 * (m + n)) + 1
    if not isSquare(a):
        return False
    b = 36 * ((n ** 2) - (m ** 2)) + (12 * (m - n)) + 1
    if not isSquare(b):
        return False
    if not (1+math.sqrt(a)) % 6 == 0:
        return False
    if not (1+math.sqrt(b)) % 6 == 0:
        return False
    return True


if __name__ == '__main__':

    n = 2
    halt = True
    while halt:
        n += 1
        print(n)
        for m in range(1, n):
           if newChecker(n,m):
                halt = False
                print(m, n)
                print((n*(3*n-1)/2)-(m*(3*m-1)/2))
                break
