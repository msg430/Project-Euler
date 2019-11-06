def giveParts(number):
    string = str(number)
    a = (int(string[0:2]), number, int(string[2:4]))
    return a



if __name__ == '__main__':

    triangle = []
    square = []
    pentagons = []
    hexagons = []
    heptagons = []
    octagons = []

    upper = 9999
    lower = 999

    n = 1
    card = 6
    halt = True
    while halt:
        n += 1

        tri = int(n*(n+1)/2)
        if tri > upper:
            halt = False
            break
        if tri > lower:
            triangle.append(tri)

        if card == 1:
            continue

        sqa = int(n**2)
        if sqa > upper:
            card = 1
            continue
        if sqa > lower:
            square.append(sqa)

        if card == 2:
            continue

        pent = int(n*(3*n-1)/2)
        if pent > upper:
            card = 2
            continue
        if pent > lower:
            pentagons.append(pent)

        if card == 3:
            continue

        hex = int(n*(2*n-1))
        if hex > upper:
            card = 3
            continue
        if hex > lower:
            hexagons.append(hex)

        if card == 4:
            continue

        hept = int(n*(5*n-3)/2)
        if hept > upper:
            card = 4
            continue
        if hept > lower:
            heptagons.append(hept)

        if card == 5:
            continue

        oct = int(n*(3*n-2))
        if oct > upper:
            card = 5
            continue
        if oct > lower:
            octagons.append(oct)

    bigHolder = [[],[],[],[],[],[]]

    for t in triangle:
        bigHolder[0].append([[1,2,3,4,5], giveParts(t)])
    for s in square:
        bigHolder[1].append(giveParts(s))
    for p in pentagons:
        bigHolder[2].append(giveParts(p))
    for h in hexagons:
        bigHolder[3].append(giveParts(h))
    for h in heptagons:
        bigHolder[4].append(giveParts(h))
    for o in octagons:
        bigHolder[5].append(giveParts(o))

    chains = bigHolder[0].copy()
    for k in range(5):
        holder = []
        for c in chains:
            last = c[len(c)-1][2]
            for left in c[0]:
                for a in bigHolder[left]:
                    if a[0] == last:
                        temp = c[0].copy()
                        temp.remove(left)
                        r = c.copy()
                        r.pop(0)
                        r = [temp] + r + [a]
                        holder.append(r)
        chains = holder.copy()

    for c in chains:
        c.pop(0)
        if c[0][0] == c[5][2]:
            this = c.copy()
            break

    summation = 0
    for c in this:
        summation += c[1]

    print(summation)
