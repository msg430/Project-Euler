import math


def getDivisors(n):
    multiples = []
    halt = True
    while halt:
        halt = False
        for d in range(2, int(math.sqrt(n))+1):
            if n % d == 0:
                count = 1
                n = int(n/d)
                while n % d == 0:
                    count += 1
                    n = int(n/d)
                multiples.append(count)
                halt = True
                break
    if n != 1:
        multiples.append(1)
    multiples.sort()
    return tuple(multiples)


def fasterNumberForN(n):
    count = 1
    for x in range(n+1, 2*n):
        hold = (n*x)/(n-x)
        if int(hold) == hold:
            count += 1
    return count


if __name__ == '__main__':

    dictionary = dict()
    limit = 1000

    n = 0
    while True:
        n += 1
        divisorCount = getDivisors(n)
        if divisorCount in dictionary:
            continue
        else:
            dictionary[divisorCount] = fasterNumberForN(n)
            if dictionary[divisorCount] > limit:
                print(n, 'has', dictionary[divisorCount])
                break

# was running at 10.061 seconds