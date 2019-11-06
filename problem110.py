import math


def nextPrime():
    primes = [2]
    yield 2
    candidate = 2
    while True:
        candidate += 1
        itsPrime = True
        for prime in primes:
            if candidate % prime == 0:
                itsPrime = False
                break
        if itsPrime:
            primes.append(candidate)
            yield candidate


def staircase(limit, primes, prior, spot):
    if primes[spot] > limit:
        yield []
    else:
        yield []
        toGoTo = min(prior+1, int(math.log(limit,primes[spot]))+1)
        for w in range(1, toGoTo):
            step = staircase(int(limit/(primes[spot]**w)), primes, w, spot+1)
            for each in step:
                yield [w] + each


def giveSecond(pair):
    return pair[1]


def nextToCheck():
    roster = [([1], 2)]
    primeGenerator = nextPrime()
    primeOnDeck = next(primeGenerator)
    primeOnDeck = next(primeGenerator)
    primeOnDeck = next(primeGenerator)
    primeOnDeck = next(primeGenerator)
    primes = [2, 3, 5]
    nextStop = 2
    lastStop = 2
    while True:
        try:
            toGive = roster.pop(0)
            yield toGive
        except IndexError:
            nextStop *= primeOnDeck
            primes.append(primeOnDeck)
            primeOnDeck = next(primeGenerator)
            stairs = staircase(nextStop, primes, int(math.log(nextStop, 2)+1), 0)
            for step in stairs:
                value = 1
                for h in range(len(step)):
                    value *= primes[h] ** step[h]
                if value > lastStop:
                    roster.append((step, value))
            lastStop = nextStop
            roster.sort(key=giveSecond)


def valueForComparison(listacle):
    if len(listacle) == 0:
        return 1
    value = 1
    for k in listacle:
        value *= (2*k)+1
    return value



if __name__ == '__main__':


    dictionary = dict()
    dictionary[()] = 1
    limit = 4000000
    giveNext = nextToCheck()
    highestValue = 0

    while True:
        current = next(giveNext)
        compareAgainst = current[0].copy()
        multiplier = compareAgainst.pop()
        if len(compareAgainst) == 0:
            hold = current[0][0]+1
            dictionary[tuple(current[0])] = hold
        else:
            hold = dictionary.get(tuple(compareAgainst)) + multiplier * valueForComparison(compareAgainst)
            dictionary[tuple(current[0])] = hold
        if hold > limit:
            print(current[1], 'has', hold)
            break
