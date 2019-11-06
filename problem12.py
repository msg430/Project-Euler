
def triangularNumbers():
    n = 1
    sum = 0
    while True:
        sum += n
        n += 1
        yield sum


def getDivisorNumber(number):
    sum = 1
    for d in range(1, int(number/2)+1):
        if number % d == 0:
            sum += 1
    return sum


if __name__ == '__main__':

    upperLimit = 500

    n = 1
    lower = 1
    while True:
        upper = getDivisorNumber(int((n+1)/2))
        if lower*upper > upperLimit:
            print(int(n*(n+1)/2))
            break
        n += 2
        lower = getDivisorNumber(n)
        if lower*upper > upperLimit:
            print(int(n * (n - 1) / 2))
            break


    # 73920 first over 100


    # number = triangularNumbers()
    # n = 0
    # highestObtained = 0
    # highestGot = 0
    # while True:
    #     n += 1
    #     current = next(number)
    #     x = getDivisorNumber(current)
    #     if x > highestGot:
    #         highestObtained = current
    #         highestGot = x
    #         print(current, 'has', x, 'divisors')
    #     if x > 500:
    #         break
    #
    # print(current)
    # print(n)
