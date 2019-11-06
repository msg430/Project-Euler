

def readInPyramid(fileName):
    file = open(fileName)
    line = file.readline()
    pyramid = []
    count = 0
    while line:
        pyramid.append([])
        numbers = line.split()
        for n in numbers:
            pyramid[count].append(int(n))
        count += 1
        line = file.readline()
    return pyramid





if __name__ == '__main__':


    pyramid = readInPyramid('/Users/matt/PycharmProjects/pyramid1.txt')
    # pyramid = readInPyramid('/Users/matt/PycharmProjects/practice_pyramid.txt')
    height = len(pyramid)

    for row in range(1, height):
        pyramid[row][0] += pyramid[row-1][0]
        pyramid[row][row] += pyramid[row-1][row-1]
        for index in range(1, row):
            pyramid[row][index] += max(pyramid[row-1][index-1], pyramid[row-1][index])
        print(pyramid)

    print(max(pyramid[height-1]))

