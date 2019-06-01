def checkPal(integer):
    number = str(integer)
    length = len(number)
    i = 0
    while i<length/2:
        if number[i] != number[length-i-1]:
            return 0
        i += 1
    return 1


largest = 0;

for i in range(100, 1000):
    for j in range(100, i+1):
        if checkPal(i*j) == 1:
            if i*j > largest:
                largest = i*j

print(largest)
