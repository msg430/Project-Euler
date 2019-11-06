import math


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3,int(math.sqrt(n))+1, 2):
        if n % d == 0:
            if n == d:
                return True
            return False
    return True


# def depth(primes, chosen, value, otherValue):

def nextThing():

    nextUp = 13
    possNext = [2, 3, 6]
    current = [5, 7, 11]
    mult = 1
    for c in current:
        mult *= c
    lowest = nextUp*mult/c
    for c in current:
        value = mult / c
        for p in possNext:
            if value * p < lowest:
                if value * p > mult:
                    lowest = value * p
    print(lowest)



def mover(primes, chosen, value, otherValue):

    for c in chosen:
        thisChosen = chosen.copy()
        thisChosen.remove(c)
        o = 0
        for k in range(c+1, len(primes)):
            if k not in chosen:
                o = k
                break
        if o > 0:
            v = int(primes[o]*value/primes[c])
            ov = int(primes[c]*otherValue/primes[o])


# def produceNext(current, length, primes, low, high, used):
#     if current == length:
#         return 0
#     else:
#         l = low * primes[current]
#         h = int(high/primes[current])
#         if l < h:
#             a = produceNext(current+1, length, primes, low, high, used)
#             b = produceNext(current+1, length, primes, l, h, used + [current])
#             return max(l, a, b)
#         else:
#             print(used + [current])
#             print(l)
#             print(h)
#             return 0

def getter(primes, values):
    mult = 1
    for v in values:
        mult *= primes[v]
    return mult


def produceNext(current, length, primes, ratio, used, checked):
    if current == length:
        checked += 1
        return getter(primes, used), checked
    else:
        h = ratio / (primes[current]**2)
        # l = low * primes[current]
        # h = int(high/primes[current])
        if h > 1:
            a, checked = produceNext(current+1, length, primes, ratio, used, checked)
            b, checked = produceNext(current+1, length, primes, h, used + [current], checked)
            return max(a, b), checked
        else:
            checked += 1
            print(used + [current])
            print(h)
            print(checked)
            return 0, checked


if __name__ == '__main__':


    # primes = [2,3,5,7,11,13,17,19]
    primes = []
    mult = 1
    for k in range(2, 190):
        if isPrime(k):
            primes.append(k)
            mult *= k
    print(primes)
    # print(produceNext(0, len(primes), primes, 1, mult, []))
    # print(produceNext(0, len(primes), primes, mult, [], 0))
    #
    # print(mult)

    h = [20, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    chosen = 1
    n = 1
    for k in range(len(primes)):
        if k in h:
            chosen *= primes[k]
        else:
            n *= primes[k]
    print(chosen)
    print(n)




    # count = 0
    # mult = 1
    # primes = []
    # for k in range(2, 190):
    #     if isPrime(k):
    #         primes.append(k)
    #         count += 1
    #         mult *= k
    # print(primes)
    #
    # mult = 1
    # for k in range(0, len(primes), 2):
    #     mult *= primes[k]
    # print(mult)
    #
    # chosen = [0]
    # possNext = []
    # nextUp = 1
    # value = primes[0]
    # otherValue = int(mult/value)
    # while True:
    #
    #     lowest = int(primes[nextUp]*value/primes[chosen[len(chosen)-1]])
    #     chip = []
    #
    #     for c in chosen:
    #         this = int(value/c)
    #         lowest = primes[nextUp]*this
    #         chip = [c, nextUp]
    #         for p in possNext:
    #             if this * p[0] < lowest:
    #                 if this * p[0] > value:
    #                     lowest =
    #             mult = 1
    #             for q in p:
    #
    #
