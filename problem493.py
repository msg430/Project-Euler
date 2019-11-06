import math


def choose(a,b):
    return int(math.factorial(a)/math.factorial(b)/math.factorial(a-b))


def dontPick(number):
    multiplier = choose(7, number)
    # print(multiplier)

    mult = 1
    for k in range(70-(number*10)-20, 70-(number*10)+1):
        mult *= k
    return mult*multiplier



if __name__ == '__main__':

    # total = 1
    # for k in range(70-20, 71):
    #     total *= k
    total = choose(70, 20)
    print(total)

    notPick = dict()
    for k in range(1, 6):
        notPick[k] = choose(7, k)*choose(70-(10*k), 20)
    print(notPick)

    actual = dict()
    for k in reversed(range(1,6)):
        a = notPick[k]
        for h in range(k+1, 6):
            a -= actual[h]
        actual[k] = a
    totalSum = 0
    for k in range(1, 6):
        totalSum += actual[k]
    print(totalSum)
    print(total)
    actual[0] = total-totalSum

    print(actual)
    expect = 0
    for k in range(6):
        prob = actual[k]/total
        expect += (7-k)*prob
        print((7-k)*prob, 7-k)
    print(expect)

    # hold = choose(20, 20) * 7
    # print(hold/total)
    # mult = 1
    # for k in range(60-20, 61):
    #     mult *= k
    # # print(7*mult/total)
    #
    # # print(dontPick(1)/total)
    #
    # s = 0
    # for x in range(1, 6):
    #     s += dontPick(x)
    #     # print(dontPick(x))
    #
    # print(s)
    # # dontPick(2)
    #

    # print(choose(60, 20)*choose(7, 6))

    t = 1
    left = 70
    # t = (math.factorial(10)**2) / (math.factorial(70)/math.factorial(50))
    for k in reversed(range(1, 11)):
        t *= k / (70-k)
        t *= k / (60 - k)
    print(t*21)
    print(21/choose(70, 20))
    print((choose(30, 20)-choose(3, 2))*choose(7,3))

    count = 1
    tot = 1
    for k in range(20):
        count *= 60-k
        tot *= 70-k
    print(count)
    print(tot)
    print(count/tot)
    print(actual[1]/total)
