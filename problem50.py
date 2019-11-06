import math


def giveSecond(pair):
    return pair[1]


def checkPrime(number):
    if number % 2 == 0:
        return False
    for n in range(3, int(math.sqrt(number) + 1), 2):
        if number % n == 0:
            return False
    return True


def checkThing(sequences, readyPrimes, notPrimes, number, primeSums, limit):
    bad = []
    for s in sequences:
        s[0] += number
        if s[0] >= limit:
            bad.append(s)
            continue
        s[1] += 1
        if checkPrime(s[0]):
            primeSums.append((s[0], s[1]))
            readyPrimes.append(s[0])
        else:
            notPrimes.append(s[0])
    sequences.append([number, 1])
    for b in bad:
        sequences.remove(b)

if __name__ == '__main__':

    sequences = [[10,3],[8,2],[5,1]]
    readyPrimes = []
    notPrimes = []
    primeSums = []

    notPrime = 0
    nextPrime = 0
    limit = 1000000
    for d in range(7, limit, 2):
        if d == notPrime:
            notPrime = notPrimes.pop(0)
            continue
        if d == nextPrime:
            nextPrime = readyPrimes.pop(0)
            checkThing(sequences, readyPrimes, notPrimes, d, primeSums, limit)
            continue
        if checkPrime(d):
            checkThing(sequences, readyPrimes, notPrimes, d, primeSums, limit)


    primeSums.sort(key=giveSecond)
    print(primeSums[len(primeSums)-1])

