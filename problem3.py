import math

number = 600851475143

factors = []


while number > 1:
#    print("testing for:", number)
    i = 2
    found = 0
    while i <= math.sqrt(number):
        if number % i == 0:
           # print(i, "divides")
            factors.append(i)
            number = number/i
            found = 1
            break
        i += 1
    if found == 0:
        factors.append(number)
        break

greatest = 1
for i in factors:
    if i > greatest:
        greatest = i

print(greatest)

