factorial = 100
number = 1
for i in range(2, factorial+1):
    number = i*number

sums = 0
string = str(number)
for i in string:
    sums = int(i)+sums

print(sums)