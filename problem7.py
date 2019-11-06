import math

counter = 2
searchTo = 10001
primes = [3]
current = 5

while len(primes) < searchTo-1:
    switch = 1
    for i in primes:
        if current % i == 0:
            switch = 0
            break
    if switch == 1:
        primes.append(current)
    current += 2

print(primes[searchTo-2])
