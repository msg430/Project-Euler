power = 1000
number = 1
for n in range(0,power):
    number = number * 2

string = str(number)
# print(string)

sums = 0
for i in string:
    sums = int(i)+sums

print(sums)