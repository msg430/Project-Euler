
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


if __name__ == '__main__':

    n = 12
    list = list(range(1, n+1))
    counter = 0
    for k in range(2, int(n/2)+1):
        pairs = recursiveChoice(list, k)
        for pair in pairs:
            holdList = list.copy()
            for x in pair:
                holdList.remove(x)
            nextPair = recursiveChoice(holdList, k)
            for next in nextPair:
                original = pair.copy()
                tempCounter = 0
                print(pair, next)
                for h in range(len(pair)):
                    if original[h] < next[h]:
                        tempCounter -= 1
                    else:
                        tempCounter += 1
                if abs(tempCounter) != len(pair):
                    counter += 1

    print(int(counter/2))
