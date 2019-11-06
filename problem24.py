import math


def numberUntil(currentlyAt, numbersLeft, limit):
    mult = math.factorial(numbersLeft - 1)
    n = -1
    while True:
        n += 1
        if n*mult+currentlyAt > limit:
            break
    # currentlyAt += mult*(n-1)
    return n-1, mult*(n-1)


if __name__ == '__main__':

    digitsUsed = 10
    limit = 1000000-1
    # digitsUsed = 3
    # limit =
    currentlyAt = 0
    places = []
    for k in range(digitsUsed-1):
        hold, toAdd = numberUntil(currentlyAt, digitsUsed-k, limit)
        currentlyAt += toAdd
        places.append(hold)
    print(places)

    digitsLeft = list(range(digitsUsed))
    print(digitsLeft)

    finalNumber = []
    for k in range(digitsUsed-1):
        # print('going to take the', places[k], 'th number from', digitsLeft)
        hold = digitsLeft.pop(places[k])
        # print(hold)
        finalNumber.append(hold)
    finalNumber.append(digitsLeft[0])
    stingList = []
    for k in finalNumber:
        stingList.append(str(k))
    A = ''.join(stingList)
    print(A)
