import math

counter = 3
primes = [2]


def isPrime(number):
    global counter
    if number < counter:
        if number in primes:
            return True
        return False
    for i in primes:
        if number % i == 0:
            return False
    while counter < math.sqrt(number)+1:
        if isPrime(counter):
            primes.append(counter)
            if number % counter == 0:
                counter += 1
                return False
        counter += 2
    return True

sums = 0
upperLimit = 2000000
for i in range(2, upperLimit):
    if isPrime(i):
        sums += i

print(sums)