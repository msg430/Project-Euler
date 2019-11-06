import math

class primeCheck:
    def __init__(self, limit):
        self.primes = [2, 3, 5]

        d = 5
        while d < limit:
            d += 1
            isPrime = True
            for p in self.primes:
                if d % p == 0:
                    isPrime = False
                    break
            if isPrime:
                self.primes.append(d)
        self.limit = limit
        self.length = len(self.primes)

    def check(self, number):
        d = 0
        factor = 0
        while d < self.length:
            if number % self.primes[d] == 0:
                factor = self.primes[d]
                break
            d += 1
        if factor == 0 or factor == number:
            return False
        number = int(number/factor)
        while d < self.length:
            if number % self.primes[d] == 0:
                if number == self.primes[d]:
                    return True
                return False
            d += 1
        return True


if __name__ == '__main__':

    upperLimit = 10**6
    primeLimit = int(math.sqrt(upperLimit))+1
    primes = [2, 3]
    for d in range(5, primeLimit, 6):
        isPrime = True
        for p in range(3, int(math.sqrt(d))+1, 2):
            if d % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(d)
        isPrime = True
        for p in range(3, int(math.sqrt(d+2)) + 1, 2):
            if (d+2) % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(d+2)

    if primes[len(primes)-1] > math.sqrt(upperLimit):
        primes.pop()

    counter = 0
    current = len(primes)-1
    nextUp = primes[current]

    primesAbove = 0

    isPrime = True

    d = 2*int(primeLimit/2)+1
    halt = True
    while halt:
        h = 1
        while primes[h] <= math.sqrt(d):
            if d % primes[h] == 0:
                isPrime = False
                break
            h += 1
        # for p in range(3, int(math.sqrt(d))+1, 2):
        #     if d % p == 0:
        #         isPrime = False
        #         break
        if isPrime:
            primesAbove += 1
            while d*nextUp > upperLimit:
                counter += primesAbove
                primesAbove += 1
                current -= 1
                nextUp = primes[current]
                if current == -1:
                    halt = False
                    break


                # try:
                #     # nextUp = primes.pop()
                #     print(nextUp)
                # except IndexError:
                #     halt = False
                #     break
        else:
            isPrime = True
        d += 2
        # h = 1
        # while primes[h] < math.sqrt(d) + 1:
        #     if d % primes[h] == 0:
        #         isPrime = False
        #         break
        #     h += 1
        # # for p in range(3, int(math.sqrt(d)) + 1, 2):
        # #     if d % p == 0:
        # #         isPrime = False
        # #         break
        # if isPrime:
        #     print(d, 'is prime')
        #     primesAbove += 1
        #     while d * nextUp > upperLimit:
        #         counter += primesAbove
        #         print(primesAbove, 'for', nextUp)
        #         primesAbove += 1
        #         current -= 1
        #         nextUp = primes[current]
        #         if current == -1:
        #             halt = False
        #             break
        #         # try:
        #         #     nextUp = primes.pop()
        #         #     print(nextUp)
        #         # except IndexError:
        #         #     halt = False
        #         #     break
        # else:
        #     isPrime = True
        # d += 4
    print(counter)

#


# 2.048 for 10^6






