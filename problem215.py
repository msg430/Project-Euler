def block(length, current, gaps):
    if length - current < 2:
        yield []
    else:
        for k in range(2, 4):
            if current+k not in gaps:
                nextOne = block(length, current+k, gaps)
                for n in nextOne:
                    yield [current+k] + n


def row(gaps, length):
    bl = block(length, 0, gaps)
    for b in bl:
        hold = b.pop()
        if hold == length:
            yield b


def giveDirection(width):
    nRow = row([], width)
    possibilities = []
    directions = []
    for r in nRow:
        possibilities.append(r)
        directions.append([])
    totalNumber = len(possibilities)
    for t in range(totalNumber):
        current = set(possibilities[t])
        for n in range(t + 1, totalNumber):
            if len(set(possibilities[n]) & current) == 0:
                directions[t].append(n)
                directions[n].append(t)
    return directions


if __name__ == '__main__':

    width = 32
    height = 10

    directions = giveDirection(width)
    totalNumber = len(directions)

    current = []
    for d in directions:
        current.append(len(d))

    for h in range(height-2):
        next = [0]*totalNumber
        for p in range(totalNumber):
            multiplier = current[p]
            for d in directions[p]:
                next[d] += multiplier
        current = next.copy()

    print(sum(current))
