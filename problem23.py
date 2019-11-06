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


def combineLists(list1, list2):
    s = set(list1)
    s.update(list2)
    return list(s)


if __name__ == '__main__':


    upperLimit = 28123
    dSum = nextDivisorSum(upperLimit)
    k = 1
    toWorkWith = []
    for j in dSum:
        if j > k:
            toWorkWith.append(k)
        k += 1


    # print(len(toWorkWith))

    found = []

    while True:
        hold = []
        try:
            current = toWorkWith.pop(0)
            print(current)
        except IndexError:
            break
        hold.append(current+current)
        for j in range(len(toWorkWith)):
            if current + toWorkWith[j] > upperLimit:
                del toWorkWith[j:]
                break
            hold.append(toWorkWith[j]+current)
        found = combineLists(hold, found)

    summation = 0
    for k in range(1, upperLimit + 1):
        if k == found[0]:
            found.pop(0)
        else:
            summation += k

    print(summation)




    # print(len(toWorkWith))

