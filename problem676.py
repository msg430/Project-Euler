import math

def removeDuplicates(masterList):
    holder = []
    for w in masterList:
        temp = set()
        for t in w:
            temp.add(t)
        if temp not in holder:
            holder.append(temp)
    replacement = []
    for w in holder:
        replacement.append(list(w))
    return replacement


def intersectionList(A,B):
    X = set(A)
    Y = set(B)
    if len(X & Y) > 0:
        return True
    return False


def giveInBase(number, base):
    current = 0
    listacle = []
    while number > 0:
        # print(number)
        hold = number % (base ** (current+1))
        listacle.append(int(hold/(base**current)))
        number -= hold
        current += 1
    listacle.reverse()
    s = ''
    for h in listacle:
        s = s + str(h)
    return s


def giveListInBase(number, base):
    current = 0
    listacle = []
    while number > 0:
        # print(number)
        hold = number % (base ** (current+1))
        listacle.append(int(hold/(base**current)))
        number -= hold
        current += 1
    listacle.reverse()
    return listacle


# given a number it returns the number of instances in the k,l range that there is equality
def giveCountForNumber(number):
    string = bin(number)[2:]
    binary = []
    for k in string:
        binary.append(int(k))
    rBinary = binary.copy()
    rBinary.reverse()
    length = len(binary)
    sums = dict()
    sums[1] = sum(binary)
    for h in range(2, 7):
        thisSum = sums[1]
        for f in range(1, h):
            for b in range(f, len(rBinary), h):
                thisSum += rBinary[b]*(2**f)
        sums[h] = thisSum
    # count = 0
    # print(number, ':', sums)
    if sums.get(3) == sums.get(1):
        print(binary)
        return True


def addSumUnder(string, spacing):
    if string == '':
        return 0
    if string == '0':
        return 0
    length = len(string)
    nextNumber = string[1:]
    if nextNumber == '':
        nextNumber = 0
    else:
        nextNumber = int(nextNumber, 2)
    count = (2**((length-1)*spacing))*(nextNumber+1) + addSumUnder(string[1:], spacing)
    temp = 0
    for j in range(length-1):
        temp += 2**(spacing*j)
    temp *= 2**(length-2)
    return int(count + temp)


def convertLimit(indexes, limit):
    return indexes
    newLimit = []
    x = 0
    for h in range(len(indexes)-1):
        if limit[indexes[h]] == 1:
            newLimit.append(indexes[h])
        else:
            thing = sum(limit[indexes[h]:indexes[h+1]])
            if thing > 0:
                newLimit.append(indexes[h])
    if limit[indexes[len(indexes)-1]] == 1:
        newLimit.append(indexes[len(indexes)-1])
    return newLimit


def newAddSumUnder(indexes, limit, tally):
    if indexes == []:
        return 1
    indexCopy = indexes.copy()
    current = indexCopy.pop()
    h = newAddSumUnder(indexCopy, limit, tally)
    if current in limit:
        for k in indexCopy:
            tally[k] += 2 ** (len(indexCopy) - 1)
        tally[current] += h
        h += 2**len(indexCopy)
    return h


def fasterAttempt(limit, k):
    inBinary = bin(limit)[2:]
    # print(inBinary)
    # print(len(inBinary))
    if (len(inBinary)-1) % k != 0:
        places = int(len(inBinary)/k)
        # print(places)
        return addSumUnder(''.join(['1']*places), k)
    else:
        string = '1'
        for h in range(k, len(inBinary), k):
            toAdd = '0'
            for j in range(k):
                if inBinary[h-j] == '1':
                    toAdd = '1'
                    break
            string += toAdd
        return addSumUnder(string, 3)


def combinations(tops):
    try:
        currentTop = tops.pop()
        deeper = combinations(tops)
        for rest in deeper:
            for k in range(currentTop+1):
                yield rest + [k]
    except IndexError:
        yield []


def possibleSums(values):
    combos = combinations([1]*len(values))
    possibles = set()
    for combo in combos:
        currentSum = 0
        for x in range(len(combo)):
            currentSum += values[x]*combo[x]
        if currentSum != 0:
            possibles.add(currentSum)
    return possibles


def iterator(values, usable, targets, runningDictionary, highest, inList):

    currentRunning = inList.copy()
    usableCopy = usable.copy()
    currentIndex = usableCopy.pop(0)
    currentValue = values[currentIndex]
    currentSum = 0
    for k in inList:
        currentSum += values[k]
    currentSum += currentValue
    if -currentSum in targets:
        runningDictionary.get(-currentSum).append(currentRunning + [currentIndex])
    if currentSum < highest and len(usableCopy) > 0:
        iterator(values, usableCopy, targets, runningDictionary, highest, currentRunning + [currentIndex])
    if len(usableCopy) > 0:
        iterator(values, usableCopy, targets, runningDictionary, highest, currentRunning)


def positivePossibilites(values, usable, targets):
    runningDictionary = dict()
    for k in targets:
        runningDictionary[k] = []
    highestWanted = -min(targets)
    usableCopy = usable.copy()
    iterator(values, usableCopy, targets, runningDictionary, highestWanted, [])
    return runningDictionary


def addOneMore(values, usable, newTarget):
    newUsable = usable.copy()
    while True:
        if len(newUsable) == 0:
            break
        current = newUsable.pop(0)
        if values[current] == newTarget:
            yield [current]
            continue
        if values[current] > newTarget:
            continue
        if values[current] < newTarget:
            if len(newUsable) > 0:
                newGenerator = addOneMore(values, newUsable, newTarget-values[current])
                for further in newGenerator:
                    yield [current] + further


# given a target value, returns sets of indexes where the values add up to the target
def possibleCombos(values, usable, target):
    tops = [1]*len(usable)
    giveThem = combinations(tops)
    for combo in giveThem:
        value = 0
        for c in range(len(usable)):
            value += combo[c]*values[usable[c]]
        if value == target:
            hold = []
            for c in range(len(usable)):
                if combo[c] == 1:
                    hold.append(usable[c])
            yield hold



    # giveThem = addOneMore(values, usable, target)
    # for h in giveThem:
    #     yield h


def giveAllCombos(indexes):
    length = len(indexes)
    tops = [1]*length
    toReturn = []
    combos = combinations(tops)
    for combo in combos:
        holder = []
        for k in range(length):
            if combo[k] == 1:
                holder.append(indexes[k])
        toReturn.append(holder)
    return toReturn


def iteration(limitValue, inPlaces, thisTotal):
    if len(inPlaces) == 0:
        return 0, 1
    places = inPlaces.copy()
    current = 2**places.pop()
    toAdd = 0
    counted = 0
    if current <= limitValue:
        toAdd += thisTotal + current
        a, b = iteration(limitValue-current, places, thisTotal + current)
        toAdd += a
        counted = b
    a, b = iteration(limitValue, places, thisTotal)
    toAdd += a
    counted += b
    return toAdd, counted


def giveValueBelow(limitValue, places):
    allowedToUse = places.copy()
    runningTotal, counted = iteration(limitValue, allowedToUse, 0)
    return runningTotal, counted


def problemChildren(k, l, limit):
    numberOfTerms = len(bin(limit)[2:])
    difference = []
    alwaysAllowedIndex = []
    negativeIndexes = []
    prePositiveIndexes = []
    for x in range(numberOfTerms):
        a = 2 ** (x % k)
        b = 2 ** (x % l)
        difference.append(a - b)
        if difference[x] < 0:
            negativeIndexes.append(x)
        elif difference[x] == 0:
            alwaysAllowedIndex.append(x)
        else:
            prePositiveIndexes.append(x)
    print(difference)
    # print(list(range(numberOfTerms)))
    negativeValues = []
    for h in negativeIndexes:
        negativeValues.append(difference[h])
    possibleNegativeSums = list(possibleSums(negativeValues))
    if len(possibleNegativeSums) > 0:
        lowestNegative = min(possibleNegativeSums)
        positiveIndexes = []
        for h in prePositiveIndexes:
            if difference[h] <= -lowestNegative:
                positiveIndexes.append(h)
        possiblePositiveSumsDictionary = positivePossibilites(difference, positiveIndexes, possibleNegativeSums)
    otherCombinationIndexes = []
    for h in possibleNegativeSums:
        negatives = possibleCombos(difference, negativeIndexes, h)
        for n in negatives:
            for p in possiblePositiveSumsDictionary.get(h):
                otherCombinationIndexes.append(n + p)
    alwaysAllowedSum = 0
    for h in alwaysAllowedIndex:
        alwaysAllowedSum += 2 ** h

    highCombos = []
    lowCombos = []
    for h in otherCombinationIndexes:
        if numberOfTerms - 1 in h:
            highCombos.append(h)
        else:
            lowCombos.append(h)

    highTotal = 0
    for h in highCombos:
        value = 0
        for x in h:
            value += 2**x
        a, b = giveValueBelow(limit - value, alwaysAllowedIndex)
        highTotal += a + value*b


    otherComboLength = len(lowCombos)

    alwaysAllowedSum *= 2 ** (len(alwaysAllowedIndex) - 1)
    # print(alwaysAllowedSum, 'always allowed sum')
    tally = [0] * numberOfTerms
    if lowCombos == []:
        lowCombos = [[]]
    for h in lowCombos:
        if numberOfTerms - 1 in h:
            print('problem')
            return 0
        digest(h, tally)
    # print(tally)
    totalSum = 0
    for x in range(numberOfTerms):
        totalSum += tally[x] * (2 ** x)
    totalSum *= 2 ** len(alwaysAllowedIndex)
    # print(totalSum, 'total sum')
    alwaysAllowedSum *= (otherComboLength + 1)
    # print(len(otherCombinationIndexes), 'always allow sum')
    totalSum += alwaysAllowedSum
    return totalSum + highTotal


def alteredThing(k, l, limit):
    numberOfTerms = len(bin(limit)[2:])
    difference = []
    alwaysAllowedIndex = []
    negativeIndexes = []
    prePositiveIndexes = []
    for x in range(numberOfTerms):
        a = 2 ** (x % k)
        b = 2 ** (x % l)
        difference.append(a - b)
        if difference[x] < 0:
            negativeIndexes.append(x)
        elif difference[x] == 0:
            alwaysAllowedIndex.append(x)
        else:
            prePositiveIndexes.append(x)
    print(difference)
    # print(list(range(numberOfTerms)))
    negativeValues = []
    for h in negativeIndexes:
        negativeValues.append(difference[h])
    possibleNegativeSums = list(possibleSums(negativeValues))
    if len(possibleNegativeSums) > 0:
        lowestNegative = min(possibleNegativeSums)
        positiveIndexes = []
        for h in prePositiveIndexes:
            if difference[h] <= -lowestNegative:
                positiveIndexes.append(h)
        possiblePositiveSumsDictionary = positivePossibilites(difference, positiveIndexes, possibleNegativeSums)
        # print('dictionary:', possiblePositiveSumsDictionary)
    otherCombinationIndexes = []
    for h in possibleNegativeSums:
        negatives = possibleCombos(difference, negativeIndexes, h)
        for n in negatives:
            for p in possiblePositiveSumsDictionary.get(h):
                otherCombinationIndexes.append(n+p)
    alwaysAllowedSum = 0
    otherComboLength = len(otherCombinationIndexes)
    for h in alwaysAllowedIndex:
        alwaysAllowedSum += 2**h
    alwaysAllowedSum *= 2**(len(alwaysAllowedIndex)-1)
    # print(alwaysAllowedSum, 'always allowed sum')
    tally = [0]*numberOfTerms
    if otherCombinationIndexes == []:
        otherCombinationIndexes = [[]]
    for h in otherCombinationIndexes:
        if numberOfTerms-1 in h:
            print('problem')
            return 0
        digest(h, tally)
    # print(tally)
    totalSum = 0
    for x in range(numberOfTerms):
        totalSum += tally[x]*(2**x)
    totalSum *= 2**len(alwaysAllowedIndex)
    # print(totalSum, 'total sum')
    alwaysAllowedSum *= (otherComboLength+1)
    # print(len(otherCombinationIndexes), 'always allow sum')
    totalSum += alwaysAllowedSum
    return totalSum


def doTheThing(k, l, limit):
    numberOfTerms = len(bin(limit)[2:])
    difference = []
    alwaysAllowedIndex = []
    for x in range(numberOfTerms):
        a = 2 ** (x % k)
        b = 2 ** (x % l)
        difference.append(a - b)
        if difference[x] == 0:
            alwaysAllowedIndex.append(x)
    preLimit = bin(limit)[2:]
    newLimit = []
    for k in preLimit:
        newLimit = [int(k)] + newLimit
    newLimit = convertLimit(alwaysAllowedIndex, newLimit)
    tally = [0]*numberOfTerms
    newAddSumUnder(alwaysAllowedIndex, newLimit, tally)
    totalSum = 0
    for h in range(numberOfTerms):
        totalSum += tally[h]*(2**h)
    return totalSum


def digest(current, tally):
    for a in range(len(current)):
        marker = current.pop()
        tally[marker] += 1


# returns True if the test is less than or equal to the limit
def listBinaryComparision(test, limit, numberOfTerms):
    binary = ''
    for place in range(numberOfTerms):
        if place in test:
            binary = '1' + binary
        else:
            binary = '0' + binary
    if int(binary, 2) > limit:
        return False
    return True


if __name__ == '__main__':

    limit = 10**16
    summation = 0
    for k in range(3, 7):
        for l in range(1, k-1):
            if (k,l) in [(5, 3), (6, 4), (4, 2)]:
                continue
            print('checking', (k, l))
            hold = alteredThing(k, l, limit)
            print('it has', hold)
            print(' ')
            summation += hold

    print('checking', (4, 2))
    hold = doTheThing(4, 2, limit)
    summation += hold
    print('it has', hold)

    print('checking', (5, 3))
    hold = problemChildren(5, 3, limit)
    summation += hold
    print('it has', hold)

    print('checking', (6, 4))
    hold = problemChildren(6, 4, limit)
    summation += hold
    print('it has', hold)



    print(summation)
    print(summation % limit)

    # print(giveValueBelow(1000, [0,2,4,8,10]))
    #
    # print(problemChildren(6,4,10**16))

    # print(giveValueBelow(1000, [0, 2, 4, 8, 10]))

    # (5,3) and (6,4) have a problem

    #
    # print(alteredThing(3, 1, 10**6))

    # limit = 10 ** 16
    # print(doTheThing(4, 1, limit))
    # print(alteredThing(4, 1, limit))
    # print(' ')
    #
    # print(doTheThing(6, 1, limit))
    # print(alteredThing(6, 1, limit))
    # print(' ')
    #
    # print(doTheThing(6, 1, limit))
    # print(alteredThing(6, 1, limit))
    # print(' ')

    # summation = 0
    # limit = 10**6
    # k = 6
    # l = 4
    # for c in range(limit+1):
    #     a = sum(giveListInBase(c, 2**k))
    #     b = sum(giveListInBase(c, 2**l))
    #     if a == b:
    #         print(c)
    #         print(bin(c)[2:])
    #
    #         summation += c
    # #
    # print('real:', summation)
    # print('found:', problemChildren(k, l, limit))
    # print('found:', alteredThing(k, l, limit))



    # print((2**17)+(2**16)+(2**15))
    # print('101000110000100011')
    # print(int('101000110000100011', 2))
    # number = int('101000110000100011', 2)
    # print(sum(giveListInBase(number, 2 ** k)))
    # print(sum(giveListInBase(number, 2 ** l)))
    #
    # # '101000110000100011'
    # # '[0, 0, 3, 6, 15, -1, 1, 2, 7, 14, 0, 0, 3, 6, 15, -1, 1, 2, 7]'
    #
    # # 11000010001100001
    # A = giveListInBase(number, 2**k)
    # B = giveListInBase(number, 2 ** l)
    # A.reverse()
    # B.reverse()
    # print(A)
    # print(B)
    #
    # print('the real one found', count)
    # # 10 10 00 11 00 00 10 00 11
    # # 101 00011 00001 00011

