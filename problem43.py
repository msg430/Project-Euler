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


def check(number, primes):
    asWord = ''
    for w in number:
        asWord += (str(w))
    for k in range(1, 8):
        number = int(asWord[k:k+3])
        if number % primes[k-1] != 0:
            return 0
    return int(asWord)


if __name__ == '__main__':

    primes = [2, 3, 5, 7, 11, 13, 17]
    totalSum = 0

    for k in range(1, 10):
        print(k)
        numbers = list(range(10))
        numbers.remove(k)
        pan = panDigital(numbers)
        for p in pan:
            totalSum += check([k]+p, primes)

    print(totalSum)
