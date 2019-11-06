seqLength = 13

file = open('/Users/matt/Desktop/number.txt')
string = file.readline()
subStrings = string.split('0')
greatest = 0


for i in subStrings:
    if len(i) < seqLength:
        subStrings.remove(i)


for i in subStrings:
    for j in range(seqLength-1, len(i)):
        holder = 1
        for k in range(0, seqLength):
            holder = holder * int(i[j-k])
        if holder > greatest:
            greatest = holder

print(greatest)


