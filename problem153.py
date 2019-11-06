import math

def isPrime(number):
    if number % 2 == 0:
        if number == 2:
            return True
        return False
    for d in range(3,int(math.sqrt(number)+1), 2):
        if number % d == 0:
            return False
    return True


def divisorSum(number):
    total = 0
    for d in range(2, int(number/2)+1):
        if number % d == 0:
            total += d
    total += number + 1
    return total


def sumOfDivs(limit):
    gaps = []
    total = 0
    for k in range(1, int(math.sqrt(limit)+1)):
        total += k*(int(limit/k))
        gaps.append(int(limit/k))
    current = int(math.sqrt(limit))+1
    left = len(gaps)
    stop = gaps.pop()
    if stop == left:
        left -= 1
        stop = gaps.pop()
    while True:
        while current < stop:
            total += current * left
            current += 1
        total += current * left
        current += 1
        left -= 1
        try:
            stop = gaps.pop()
        except IndexError:
            break
    return total


if __name__ == '__main__':

    limit = 10**8

    total = 0
    for x in range(1, int(math.sqrt(limit))+1):
    # for x in range(1, 200):
        print(x)
        for y in range(1, int(math.sqrt(limit-(x**2))+1)):
            # print(y)
            gcd = int(math.gcd(x, y))
            if gcd == 1:
                upTo = int(limit/((x**2)+(y**2)))
                total += (upTo*(upTo+1)+(upTo-1)*2)*x
            else:
                a = int(x/gcd)
                u = int(int(limit/((a**2)+(int(y/gcd)**2)))/gcd)
                total += 2 * (u-gcd+1)*x + a*(u*(u+1) - (gcd*(gcd+1)))

    # print('here')

    print(sumOfDivs(limit)+total)

#     to 200: 4.638
