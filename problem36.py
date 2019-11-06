
def checkBinary(number):
    number = int(number)
    inBinary = bin(number)[2:]
    backwards = inBinary[::-1]
    if inBinary == backwards:
        return True
    return False


if __name__ == '__main__':

    limit = 1000000
    a = 1
    digitLimit = 0
    while True:
        a *= 10
        digitLimit += 1
        if a >= limit:
            break

    works = []
    for k in range(1, 10**(int(digitLimit/2))):
        first = str(k)
        second = first[::-1]
        if k < 100:
            for l in range(10):
                current = first + str(l) + second
                if checkBinary(current):
                    print(current)
                    works.append(int(current))
        current = first+second
        if checkBinary(current):
            print(current)
            works.append(int(current))

    for k in range(1,10):
        if checkBinary(str(k)):
            print(k)
            works.append(k)

    print(sum(works))

