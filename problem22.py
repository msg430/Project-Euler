




if __name__ == '__main__':

    file = open('/Users/Matt/PycharmProjects/p022_names.txt')
    line = file.readline()

    names = []
    preNames = line.split(',')
    for k in preNames:
        names.append(k.strip('"'))

    names.sort()

    totalSum = 0
    for k in range(len(names)):
    # for k in range(937, 940):
    #     print(names[k])
        nameSum = 0
        for j in names[k]:
            nameSum += ord(j) - ord('A') + 1
        totalSum += nameSum * (k+1)

    print(totalSum)



