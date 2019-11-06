

number = 0
for k in range(1, 1001):
    number += k**k
string = str(number)
print(string[len(string)-11:])
