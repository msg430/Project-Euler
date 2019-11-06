import math

results = []
highestValue = 0
highestObtained = 0

upperLimit = 1000
for D in range(2, upperLimit + 1):
    r = int(math.sqrt(D))
    if r * r == D:
        continue


    a = [int(math.sqrt(D))]
    P = [0]
    Q = [1]

    k = 0
    while True:
        k += 1
        P.append(a[k-1]*Q[k-1]-P[k-1])
        Q.append(int((D-(P[k]**2))/Q[k-1]))
        a.append(int((math.sqrt(D)+P[k])/Q[k]))
        if Q[k] == 1:
            break

    if k % 2 != 0:
        l = a.copy()
        l.pop(0)
        for h in l:
            a.append(h)

    a.pop()

    top = a.pop()
    bottom = 1
    while True:
        try:
            next = a.pop()
        except IndexError:
            break
        lTop = bottom
        lBottom = top
        top = lBottom*next+lTop
        bottom = lBottom

    gcd = math.gcd(top, bottom)
    top = int(top/gcd)
    bottom = int(bottom/gcd)
    print((D,top))
    results.append((D,top))
    if top > highestValue:
        highestValue = top
        highestObtained = D

print('the winner is', highestObtained, 'with', highestValue)
