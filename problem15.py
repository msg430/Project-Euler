def pathNumber(x, y):
    if x==-1 or y==-1:
        return 0
    if (x, y) in dictionary:
        return dictionary.get((x, y))
    dictionary[(x, y)]=dictionary[(y, x)]=pathNumber(x-1, y)+pathNumber(x, y-1)
    return dictionary.get((x, y))

dictionary = dict()

dictionary[(0,1)] = 1
dictionary[(1,0)] = 1


print(pathNumber(20,20))