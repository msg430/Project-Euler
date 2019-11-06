

def getNumber(word):
    total = 0
    for digit in word:
        total += ord(digit)-64
    return total


if __name__ == '__main__':

    file = open('/Users/Matt/PycharmProjects/words.txt')

    preWords = file.readline()


    preWords = preWords.split(',')
    words = []
    for w in preWords:
        words.append(w[1:len(w)-1])

    triangles = []
    for n in range(100):
        triangles.append(int(n*(n+1)/2))

    count = 0
    for w in words:
        if getNumber(w) in triangles:
            count += 1

    print(count)

