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


if __name__ == '__main__':

    file = open('/Users/Matt/PycharmProjects/p105_sets.txt')
    currentSet = file.readline()
    totalSum = 0
    for line in file:
        line = line.split(',')
        currentSet = []
        for k in line:
            currentSet.append(int(k))
        if isSpecial(currentSet):
            totalSum += sum(currentSet)

    print(totalSum)


