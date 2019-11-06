import math


def divisors(number):
    divisors = []
    if number % 2 == 0:
        divisors.append(2)
        number = int(number/2)
        while number % 2 == 0:
            number = int(number / 2)
    d = 3
    halt = True
    while halt:
        halt = False
        for d in range(3,int(math.sqrt(number)+1),2):
            if number % d == 0:
                divisors.append(d)
                halt = True
                number = int(number/d)
                while number % d == 0:
                    number = int(number / d)
                break
        if number == 1:
            break
    if number > 1:
        divisors.append(number)
    return divisors


if __name__ == '__main__':

    # n = 6
    # print(n)
    # print(divisors(n))
    limit = 10**5

    # totalSum = 0
    # for n in range(1, limit+1):
    #     found = True
    #     for x in range(1, int(n/2)+1):
    #         if (x**2 % n) == n-x:
    #             totalSum += n-x
    #             found = False
    #             break
    #     if found:
    #         totalSum += 1
    #
    #
    # print(totalSum)

    # n = 914
    # for x in range(1, n):
    #     if (x**2 % n) == x:
    #         print(x)
    #

    totalSum = 1
    doneHigh = 1
    done = []
    halt = True
    d = 1
    while halt:
        d += 1
        if 2*d > doneHigh:
            doneHigh += 1
            # print(doneHigh, 1)
            totalSum += 1
        # print(d)
        hold = (d**2)+d
        lim = min(limit+1, hold+1)
        for n in range(doneHigh+1, lim):
            if hold % n == 0:
                if n not in done:
                    # print(n, n-d)
                    totalSum += n-d
                    done.append(n)
        done.sort()
        while len(done) > 0:
            if done[0] == doneHigh + 1:
                doneHigh += 1
                done.pop(0)
            else:
                break
        if doneHigh == limit:
            halt = False

    print(totalSum)
    