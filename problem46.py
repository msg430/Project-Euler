import math

class Checker:
    def __init__(self):
        self.primes = [2,3,5]
        self.highestPrime = 5

    def check(self, number):
        if number > self.highestPrime:
            self.movePrime(number)
        if number in self.primes:
            return True
        for p in self.primes:
            h = int((number-p)/2)
            l = int(math.sqrt(h))
            if l**2 == h:
                return True
        return False

    def movePrime(self, number):
        for d in range(self.highestPrime+1, number+1):
            isPrime = True
            for p in self.primes:
                if d % p == 0:
                    isPrime = False
                    break
            if isPrime:
                self.primes.append(d)
        self.highestPrime = number


if __name__ == '__main__':

    checker = Checker()

    n = 1
    while True:
        n += 2
        if not checker.check(n):
            print(n)
            break
