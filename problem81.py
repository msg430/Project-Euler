matrix = dict()
dictionary = dict()
width = 80
# width = 5


def shortestSum(x, y):
    if (x, y) in dictionary:
        return dictionary.get((x, y))
    if x == width-1:
        if y == width-1:
            dictionary[(x, y)] = matrix.get((x, y))
            return matrix.get((x, y))
        dictionary[(x, y)] = matrix.get((x,y)) + shortestSum(x, y+1)
        return dictionary.get((x, y))
    if y == width-1:
        dictionary[(x, y)] = matrix.get((x, y)) + shortestSum(x+1, y)
        return dictionary.get((x, y))
    dictionary[(x, y)] = matrix.get((x, y)) + min(shortestSum(x+1, y), shortestSum(x, y+1))
    return dictionary[(x,y)]


file = open('/Users/matt/Desktop/p081_matrix.txt')
# file = open('/Users/matt/Desktop/practice.txt')
for i in range(0, width):
    bits = file.readline().split(',')
    for k in range(0, width):
        matrix[(k, i)] = int(bits[k])

print(shortestSum(0,0))
