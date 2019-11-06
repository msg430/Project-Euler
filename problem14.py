upperLimit = 1000000

recordNumber = 1
recordSetter = 1

dictionary = dict()

# for n in [13]:
for k in range(2,upperLimit):
    n = k
    counter = 1
    while n!= 1:
        if n in dictionary:
            # print('adding', dictionary.get(n), 'to', counter, 'for', k)
            counter = counter + dictionary.get(n) - 1
            break
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        counter += 1
    dictionary[k] = counter
    if counter > recordNumber:
        recordNumber = counter
        recordSetter = k

print(recordSetter)

