file = open('/Users/matt/Desktop/numbers.txt')

sums = 0
line = file.readline()
while line:
    sums += int(line)
    print(line)
    line = file.readline()

number = str(sums)
print(number[0:10])