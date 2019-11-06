

def doNext(coins, numberLeft):
    if numberLeft == 0:
        return 1
    leftCopy = numberLeft
    coinCopy = coins.copy()
    try:
        current = coinCopy.pop(0)
    except IndexError:
        return 0
    summation = 0
    while leftCopy >= 0:
        summation += doNext(coinCopy, leftCopy)
        leftCopy -= current
    return summation


if __name__ == '__main__':

    lookingFor = 200

    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    num = doNext(coins, lookingFor)
    print(num)
