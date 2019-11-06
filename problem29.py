numbers = set([])

upper = 100

for a in range(2,upper + 1):
    for b in range(2,upper + 1):
        base = 1
        for k in range(0,b):
            base = base * a
        numbers.add(base)

print(len(numbers))
