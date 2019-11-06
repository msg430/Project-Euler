import math
import copy


def combinations(tops):
    try:
        currentTop = tops.pop()
        deeper = combinations(tops)
        for rest in deeper:
            for k in range(currentTop+1):
                yield rest + [k]
    except IndexError:
        yield []


def divisorSum(divisorLists):
    length = len(divisorLists[0])
    combos = combinations(divisorLists[1].copy())
    divisorSummation = 0
    for currentCombo in combos:
        currentMultiple = 1
        for k in range(length):
            currentMultiple *= divisorLists[0][k]**currentCombo[k]
        divisorSummation += currentMultiple
    divisorSummation -= currentMultiple
    return divisorSummation


def nextDivisorSum(upperLimit):
    divisorDictionary = dict()
    divisorDictionary[2] = [[2], [1]]
    yield 0 # for 1
    yield 0 # for 2
    currentNumber = 2
    while currentNumber < upperLimit:
        currentNumber += 1
        divisor = 1
        for d in range(2, int(math.sqrt(currentNumber)) + 1):
            if currentNumber % d == 0:
                divisor = d
                break
        if divisor == 1:
            divisorDictionary[currentNumber] = [[currentNumber], [1]]
            yield 0
        else:
            if divisorDictionary[int(currentNumber/divisor)] == 0:
                divisorDictionary[currentNumber] = 0
                yield 0
                continue
            divisorDictionary[currentNumber] = copy.deepcopy(divisorDictionary[int(currentNumber/divisor)])
            try:
                index = divisorDictionary[currentNumber][0].index(divisor)
                divisorDictionary[currentNumber][1][index] += 1
            except ValueError:
                divisorDictionary[currentNumber][0].append(divisor)
                divisorDictionary[currentNumber][1].append(1)
            hold = divisorSum(divisorDictionary[currentNumber])
            if hold > upperLimit:
                divisorDictionary[currentNumber] = 0
                yield 0
                continue
            yield divisorSum(divisorDictionary[currentNumber])


def findLoop(dictionary, currentlyAt, hitSoFar):
    thisTrail = hitSoFar.copy()
    thisTrail.append(currentlyAt)
    try:
        thisPage = dictionary.pop(currentlyAt)
    except KeyError:
        return [False]
    for earlier in thisPage:
        if earlier == thisTrail[0]:
            return [True, thisTrail]
        h = findLoop(dictionary, earlier, thisTrail)
        if h[0]:
            return h
    return [False]


if __name__ == '__main__':

    upperLimit = 1000000
    dictionary = dict()

    divisorSummation = nextDivisorSum(upperLimit)

    currentCount = 0
    for k in divisorSummation:
        currentCount += 1
        if k in dictionary:
            dictionary.get(k).append(currentCount)
        else:
            dictionary[k] = [currentCount]

    poppedOff = 0

    current = dictionary.get(0)
    while True:
        try:
            this = current.pop()
            poppedOff += 1
        except IndexError:
            break
        if this in dictionary:
            current.extend(dictionary.pop(this))

    cycles = []
    keys = list(dictionary.keys())
    while len(keys) > 0:
        currentThing = findLoop(dictionary, keys[0], [])
        if currentThing[0]:
            cycles.append(currentThing[1])
        keys = list(dictionary.keys())

    longestLength = 0
    for k in range(len(cycles)):
        if len(cycles[k]) > longestLength:
            longestLength = len(cycles[k])
            longestIndex = k

    longestCycle = cycles[longestIndex]
    print(min(longestCycle))
