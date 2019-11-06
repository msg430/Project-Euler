


def getPrimes():
    primes = [2,3,5]
    for d in range(6,10000):
        isPrime = True
        for p in primes:
            if d % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(d)
    for p in range(len(primes)):
        if primes[p] > 999:
            hold = p
            break
    primes = primes[hold:len(primes)]
    return primes


def perms(num1, num2):
    a = list(str(num1))
    b = list(str(num2))
    a.sort()
    b.sort()
    if a == b:
        return True
    return False


if __name__ == '__main__':

    primes = getPrimes()
    progressions = []
    while True:
        try:
            current = primes.pop(0)
        except IndexError:
            break
        thisProgression = []
        for p in primes:
            if perms(current, p):
                thisProgression.append(p)
        for p in thisProgression:
            primes.remove(p)
        thisProgression.append(current)
        if len(thisProgression) > 2:
            progressions.append(thisProgression)

    candidates = []
    for p in progressions:
        pairs = []
        for a in range(len(p)-1):
            for b in range(a+1, len(p)):
                pairs.append((abs(p[b]-p[a]), a,b))
        dictionary = dict()
        for a in pairs:
            if a[0] in dictionary:
                dictionary[a[0]] += 1
            else:
                dictionary[a[0]] = 1
        poss = []
        for a in dictionary.keys():
            if dictionary[a] >= 2:
                poss.append(a)
        for k in poss:
            hold = set()
            for a in pairs:
                if a[0] == k:
                    hold.add(p[a[1]])
                    hold.add(p[a[2]])
            hold = list(hold)
            hold.sort()
            length = len(hold)
            base = hold[1]-hold[0]
            bad = True
            for k in range(2,length):
                if hold[k]-hold[k-1] != base:
                    bad = False
                    break
            if bad:
                candidates.append(hold)

    print(candidates)


