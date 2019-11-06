import math


def quickDivs(input):
    primes = []
    number = input

    while number % 2 == 0:
        primes.append(2)
        number = int(number/2)

    caught = True
    while caught:
        caught = False
        for d in range(3, int(math.sqrt(number)+1), 2):
            if number % d == 0:
                caught = True
                while number % d == 0:
                    primes.append(d)
                    number = int(number/d)
                break
    if number > 1:
        primes.append(number)

    primes = list(set(primes))
    primes.sort()
    return primes


def subThing(depth):
    adder = 3
    if depth % 2 == 0:
        adder += 3
    poss = math.floor((depth - adder - 1) / 6) + 1
    return poss


def otherCombos(input):
    if len(input) == 0:
        yield []
    else:
        this = input.copy()
        current = this.pop(0)
        for y in range(current+1):
            deeper = otherCombos(this)
            for d in deeper:
                yield [y]+d


def independent(depth):
    primes = quickDivs(depth)
    tops = []
    for p in primes:
        hold = depth
        temp = 0
        while hold % p == 0:
            hold = int(hold/p)
            temp += 1
        tops.append(temp)
    length = len(primes)
    divisors = []
    for c in otherCombos(tops):
        mult = 1
        for l in range(length):
            mult *= primes[l]**c[l]
        divisors.append(mult)
    divisors.remove(1)
    divisors.remove(depth)
    poss = subThing(depth)
    if len(divisors) == 0:
        return poss
    for d in divisors:
        poss -= independent(d)
    return poss


if __name__ == '__main__':

    walls = 12017639147
    depth = int((walls + 3) / 2)
    print(2*independent(depth))
