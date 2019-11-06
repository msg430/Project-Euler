import math


class PrimeCheck:
    def __init__(self, upperLimit):
        self.highestNumber = 1
        self.primes = [2]
        self.given = -1
        self.used = []
        self.upperLimit = upperLimit
        for d in range(3, int(math.sqrt(upperLimit))+1):
            isPrime = True
            for p in self.primes:
                if d % p == 0:
                    isPrime = False
            if isPrime:
                self.primes.append(d)

    def check(self, number):
        for p in self.primes:
            if number % p == 0:
                if number != p:
                    return False
                else:
                    return True
        return True

    def nextPrime(self):
        while True:
            self.highestNumber += 1
            if self.highestNumber > self.upperLimit:
                return 0
            if self.check(self.highestNumber):
                return self.highestNumber


def rearranger(number):
    numbers = set()
    numbers.add(number)
    number = str(number)
    for w in range(len(number)-1):
        number = number[1:] + number[0]
        numbers.add(int(number))
    return list(numbers)


if __name__ == '__main__':

    upperLimit = 1000000

    checker = PrimeCheck(upperLimit)
    current = checker.nextPrime()
    goodOnes = set()

    while current != 0:
        combo = rearranger(current)
        works = True
        for c in combo:
            if not checker.check(c):
                works = False
                break
        if works:
            for c in combo:
                goodOnes.add(c)
        current = checker.nextPrime()

    print(goodOnes)
    print(len(goodOnes))
