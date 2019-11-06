import math


def panDigital(numbers):
    length = len(numbers)
    if length == 0:
        yield []
    else:
        for k in numbers:
            theseNumbers = numbers.copy()
            theseNumbers.remove(k)
            nextLevel = panDigital(theseNumbers)
            for j in nextLevel:
                yield [k] + j


def isPrime(number):
    if number[len(number)-1] == 2:
        return False
    tester = ''
    for n in number:
        tester = tester + str(n)
    number = int(tester)
    for d in range(3, int(math.sqrt(number))+1,2):
        if number % d == 0:
            return False
    return True


if __name__ == '__main__':

    found = False
    for j in reversed(range(1,10)):
        if found:
            break
        numbers = list(reversed(range(1, j+1)))
        pan = panDigital(numbers)
        for p in pan:
            if isPrime(p):
                print(p)
                found = True
                break
