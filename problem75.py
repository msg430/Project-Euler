import math


def nextSquare(upperLimit):
    x = 1
    upper = int(upperLimit/2)
    while x < upper:
        yield x, x**2
        x += 1




if __name__ == '__main__':

    # for 1000: there are 112 and it takes 0.32 seconds
    # for 10000: there are 1120 and it takes 11.86 seconds
    upperLimit = 100

    # square = nextSquare(upperLimit)
    #
    #
    # # small, big = next(square)
    #
    holder = math.sqrt(2)
    # stack = []
    # for small, big in square:
    #     for k in range(1, int(small/holder)+1):
    #         # if big - (k**2) in squares:
    #         #     stack.append(small + k + int(math.sqrt(big - (k**2))))
    #         h = big - (k**2)
    #         r = int(math.sqrt(h))
    #         if r**2 == h:
    #             stack.append(small+k+r)
    #
    # dictionary = dict()
    # for k in stack:
    #     if k > upperLimit:
    #         continue
    #     if k in dictionary:
    #         dictionary[k] += 1
    #     else:
    #         dictionary[k] = 1
    #
    # sum = 0
    # for k in dictionary:
    #     if dictionary[k] == 1:
    #         sum += 1
    #
    # print(sum)

    stack = []
    for a in range(2, int(upperLimit/2)):
        aSquare = a**2
        for b in range(1, a+1):
            h = aSquare + (b**2)
            r = int(math.sqrt(h))
            if r*r == h:
                stack.append(a + b + r)

    dictionary = dict()
    for k in stack:
        if k > upperLimit:
            continue
        if k in dictionary:
            dictionary[k] += 1
        else:
            dictionary[k] = 1

    sum = 0
    for k in dictionary:
        if dictionary[k] == 1:
            sum += 1

    print(sum)

    print(dictionary)