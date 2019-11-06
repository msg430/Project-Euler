

def recursiveChoice(list, leftToChoose):
    if leftToChoose == 0:
        yield []
    else:
        stopper = len(list)-leftToChoose+1
        stepList = list.copy()
        for h in range(stopper):
            holder = stepList.pop(0)
            nextStep = recursiveChoice(stepList, leftToChoose-1)
            for step in nextStep:
                yield [holder] + step


# given a subset of list, gives every other subset that has the same number or less elements
def giveEveryOther(list, subset):
    maxSize = len(subset)
    holdingList = list.copy()
    for k in subset:
        holdingList.remove(k)
    for w in range(1, maxSize+1):
        otherSets = recursiveChoice(holdingList, w)
        for otherSet in otherSets:
            yield otherSet


def isSpecial(list):
    lengthOfList = len(list)

    for y in range(1, lengthOfList):
        subsets = recursiveChoice(list, y)
        for subset in subsets:
            subsetSum = sum(subset)
            others = giveEveryOther(list, subset)
            for other in others:
                otherSum = sum(other)
                if otherSum == subsetSum:
                    # print(subset, 'and', other, 'are a problem')
                    return False
                if len(other) < len(subset):
                    if otherSum > subsetSum:
                        # print(subset, 'and', other, 'are a problem')
                        return False
    return True


def addOneIn(list, knownLowest, lengthWanted):
    if len(list) == lengthWanted:
        yield []
    else:
        leftToAdd = lengthWanted - len(list)
        currentList = list.copy()
        lastNumber = currentList.pop()
        currentSum = lastNumber
        lowestAllowed = 1
        if len(currentList) > 0:
            currentSum += sum(currentList)
            lowestAllowed = currentList[len(currentList)-1]+1
        lengthWanted - len(currentList) - 1
        for t in range(lowestAllowed, lastNumber-lengthWanted+len(currentList)+2):
            if currentSum + t*leftToAdd + (leftToAdd*(leftToAdd-1)/2) <= knownLowest:
                holdList = currentList + [t, lastNumber]
                if not isSpecial(holdList):
                    continue
                furtherList = addOneIn(holdList, knownLowest, lengthWanted)
                for further in furtherList:
                    yield [t] + further




if __name__ == '__main__':

    sets = [11, 18, 19, 20, 22, 25]
    checker = [20, 31, 38, 39, 40, 42, 45]
    print(checker)
    print(sum(checker))
    bottom = 29
    print(6*bottom + (1+2+3+4+5) + bottom + bottom)
    print('top is', bottom+bottom)
    print(isSpecial(checker))

    for n in range(7, 59):
        print('checking', n)
        poss = addOneIn([n], 255, 7)
        for p in poss:
            print(p + [n])
