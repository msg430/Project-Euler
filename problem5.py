import math


def isPrime(number):
    j = 2
    while j <= math.sqrt(number):
        if number % j == 0:
            return 0
        j += 1
    return 1


i = 0
biggest = 20
primeMultiple = 1

for k in range(1, biggest+1):
    if isPrime(k) == 1:
        primeMultiple = primeMultiple*k

counter = primeMultiple

while i == 0:
    for j in range(2, biggest+1):
        if counter % j != 0:
            break
        if j == biggest:
            i = 1
    counter += primeMultiple



print(counter-primeMultiple)

