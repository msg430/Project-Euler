import math

pairCount = 5


counter = 3
primes = [2]
primeSets = []
switch = False

for m in range(0, pairCount-1):
    primeSets.append([])


def howFar():
    for t in range(0, pairCount - 2):
        smallest = sum(primeSets[t][0])
        for j in primeSets[t]:
            if sum(j) < smallest:
                smallest = sum(j)
        if (biggest - smallest)/(pairCount-2-t) > counter:
            return int((biggest - smallest)/(pairCount-2-t))+1
    return 0


def better(number):
    for i in primes:
        if number % i == 0:
            return False
    primes.append(number)
    appendPrime(number)
    return True


def altCheck(number):
    for i in primes:
        if number % i == 0:
            return False
    f = counter
    while f < math.sqrt(number)+1:
        if number % f == 0:
            return False
        f += 2
    return True


def doesTheThing(a, b):
    if a == b:
        return False
    a = str(a)
    b = str(b)
    if altCheck(int(a+b)):
        if altCheck(int(b+a)):
            return True
    return False


def appendPrime(p):
    holder = []
    for i in range(1, len(primes)):
        if switch:
            if p + primes[i] < biggest:
                if doesTheThing(p, primes[i]):
                    primeSets[0].append([p, primes[i]])
                    holder.append(primes[i])
        else:
            if doesTheThing(p, primes[i]):
                primeSets[0].append([p, primes[i]])
                holder.append(primes[i])
    for k in range(0, pairCount-2):
        for j in primeSets[k]:
            check = True
            for l in j:
                if l not in holder:
                    check = False
                    break
            if check:
                former = j.copy()
                former.append(p)
                primeSets[k+1].append(former)


while len(primeSets[pairCount-2]) == 0:
    better(counter)
    counter += 2

biggest = 0
for k in primeSets[pairCount-2]:
    biggest = max(sum(k), biggest)

switch = True

print(biggest)
print('counter is at:', counter)

while counter < biggest+2:
    better(counter)
    counter += 2
    if counter % 1001 == 0:
        print('counter at:', counter)

least = biggest
for k in primeSets[pairCount-2]:
    least = min(sum(k), least)

print(least)

# print('primes:', primes)
# print('pairs:', primeSets[0])
# print('triples:', primeSets[1])
# print('quads:', primeSets[2])
print('quints:', primeSets[3])
