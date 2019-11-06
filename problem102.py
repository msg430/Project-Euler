
def sign(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    if x < 0:
        return -1


def sameSide(coords):
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    x3 = coords[4]
    y3 = coords[5]
    if x1 == x2:
        if sign(x1-x3) == sign(x1):
            return True
        return False
    m=(y2-y1)/(x2-x1)
    b=y1-x1*m
    height = m*x3+b
    if sign(height-y3) == sign(b):
        return True
    return False


def convertFormat(line):
    line = line.rstrip()
    string = line.split(',')
    triangle = []
    for bits in string:
        triangle.append(int(bits))
    return triangle


if __name__ == '__main__':

    file = open('/Users/matt/PycharmProjects/traingles.txt')
    line = file.readline()

    sum = 0
    while line:
        triangle = convertFormat(line)
        for x in range(3):
            if not sameSide(triangle):
                break
            if x == 2:
                sum += 1
            triangle.append(triangle.pop(0))
            triangle.append(triangle.pop(0))
        line = file.readline()

    print(sum)