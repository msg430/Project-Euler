

def isPrime(number, primes):
    highestPrime = primes[len(primes)-1]
    if number <= highestPrime:
        if number in primes:
            return True
        return False
    for d in range(highestPrime+1, number):
        itIs = True
        for prime in primes:
            if d % prime == 0:
                itIs = False
                break
        if itIs:
            primes.append(d)
    for prime in primes:
        if number % prime == 0:
            return False
    primes.append(number)
    return True


def runLength(a, b, low, high, primes):
    for n in range(low, high):
        if not isPrime((n**2) + (a*n) + b, primes):
            return False, n


def findPlace(thingy):
    return -thingy[1]


if __name__ == '__main__':

    bounds = 1000
    primes = [2]
    isPrime(bounds, primes)

    step = 1000
    currentlyAt = 0

    stack = []
    for b in primes:
        if b > bounds:
            break
        for a in range(-bounds+1, bounds):
            stack.append([a, b])

    while True:
        altStack = []
        holding = []
        numberLeft = len(stack)
        print('there are', numberLeft, 'left')
        for k in range(numberLeft):
            current = stack.pop()
            x, y = runLength(current[0], current[1], currentlyAt, currentlyAt+step, primes)
            if x:
                altStack.append(current)
            else:
                holding.append((current, y))
        stack = altStack.copy()
        altStack = []
        currentlyAt += step
        if len(stack) == 0:
            holding.sort(key=findPlace)
            winner = holding[0]
            break
        if len(stack) == 1:
            winner = stack[0]
            break

    print('the winner is the pair', (winner[0][0], winner[0][1]), 'with at least', currentlyAt, 'primes')
    print('and has product', winner[0][0]*winner[0][1])
