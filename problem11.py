

def readInGrid(fileName):
    grid = dict()
    file = open(fileName)
    line = True
    h = -1
    while line:
        h += 1
        w = -1
        line = file.readline()
        numbers = line.split()
        for n in numbers:
            w += 1
            n = int(n)
            grid[(w, h)] = n
    return grid, h


def checkHorizontal(grid, height):
    max = 0
    for y in range(height):
        for x in range(0, height-3):
            current = 1
            for z in range(4):
                current *= grid.get((x+z, y))
            if current > max:
                max = current
    return max


def checkVertical(grid, height):
    max = 0
    for y in range(height-3):
        for x in range(0, height):
            current = 1
            for z in range(4):
                current *= grid.get((x, y+z))
            if current > max:
                max = current
    return max


def checkDownDiagonal(grid, height):
    max = 0
    for x in range(height-3):
        for y in range(height-3):
            current = 1
            for z in range(4):
                current *= grid.get((x+z, y+z))
            if current > max:
                max = current
    return max

def checkUpDiagonal(grid, height):
    max = 0
    for x in range(height-3):
        for y in range(3, height):
            current = 1
            for z in range(4):
                current *= grid.get((x+z, y-z))
            if current > max:
                max = current
    return max


if __name__ == '__main__':

    grid, height = readInGrid('/Users/Matt/PycharmProjects/grid11.txt')


    a = checkHorizontal(grid, height)
    b = checkVertical(grid, height)
    c = checkDownDiagonal(grid, height)
    d = checkUpDiagonal(grid, height)

    print(a)
    print(b)
    print(c)

    print(max(a,b,c,d))

    print(17*20)