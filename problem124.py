import math

def takeFirst(elem):
    return elem[0]


def nextCombo(highestAllowed):
    runningCombos = [[6, 2, 3]]
    yield [1, 1]
    yield [2, 2]
    yield [3, 3]
    usedCombos = [[2, 2], [3, 3]]
    getPrime = nextPrime()
    primeNumber = next(getPrime)
    primeNumber = next(getPrime)
    primeNumber = next(getPrime)
    while len(runningCombos) > 0:
        if primeNumber < runningCombos[0][0]:
            for h in range(len(runningCombos)):
                hold = runningCombos[h].copy()
                hold[0] *= primeNumber
                if hold[0] > highestAllowed:
                    break
                hold.append(primeNumber)
                runningCombos.append(hold)
            for l in usedCombos:
                hold = l.copy()
                hold[0] *= primeNumber
                if hold[0] > highestAllowed:
                    break
                hold.append(primeNumber)
                runningCombos.append(hold)
            usedCombos.append([primeNumber, primeNumber])
            runningCombos.sort(key=takeFirst)
            yield [primeNumber, primeNumber]
            primeNumber = next(getPrime)
        else:
            hold = runningCombos.pop(0)
            yield hold
            usedCombos.append(hold)


def nextPrime():
    primes = []
    k = 1
    while True:
        k += 1
        prime = True
        for p in primes:
            if k % p == 0:
                prime = False
                break
        if prime:
            primes.append(k)
            yield k


def combinations(tops):
    try:
        currentTop = tops.pop()
        deeper = combinations(tops)
        for rest in deeper:
            for k in range(currentTop):
                yield rest + [k]
    except IndexError:
        yield []


if __name__ == '__main__':

    highestAllowed = 100000
    lookingFor = 10000

    combo = nextCombo(highestAllowed)
    current = next(combo)
    counter = 1
    while True:
        current = next(combo).copy()
        multiple = current.pop(0)
        tops = []
        numberOfPrimes = len(current)
        for prime in current:
            tops.append(int(math.log(int(prime*highestAllowed/multiple), prime))+1)
        powers = combinations(tops)
        presentList = []
        for power in powers:
            currentCombination = multiple
            for j in range(numberOfPrimes):
                currentCombination *= current[j]**power[j]
            if currentCombination <= highestAllowed:
                presentList.append(currentCombination)
        if len(presentList) + counter >= lookingFor:
            presentList.sort()
            print(presentList[lookingFor-counter-1])
            break
        else:
            counter += len(presentList)
