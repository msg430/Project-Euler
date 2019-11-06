def pushUp(matrix, row):
    if row == 0:
        thisDictionary = dict()
        for r in range(len(matrix)):
            thisDictionary[tuple([r])] = matrix[row][r]
        return thisDictionary
    aboveDictionary = pushUp(matrix, row-1)
    keys = aboveDictionary.keys()
    thisDictionary = dict()
    for r in range(len(matrix)):
        for k in keys:
            if r not in k:
                hold = list(k)
                hold.append(r)
                hold.sort()
                hold = tuple(hold)
                value = aboveDictionary[k] + matrix[row][r]
                if hold in thisDictionary:
                    thisDictionary[hold] = max(thisDictionary[hold], value)
                else:
                    thisDictionary[hold] = value
    return thisDictionary


if __name__ == '__main__':

    file = open('/Users/Matt/PycharmProjects/245matrix.txt')
    width = 15

    matrix = []
    for k in range(width):
        matrix.append([])
    row = 0
    for f in file:
        f = f.split()
        column = 0
        for each in f:
            matrix[row].append(int(each))
            column += 1
        row += 1

    d = pushUp(matrix, width-1)
    for k in d.keys():
        print(d[k])
