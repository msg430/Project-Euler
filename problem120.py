runningCounter = 0

for a in range(3, 1001):
    print(a)
    most = max((2 * a) % (a * a), 2)
    for n in range(1, (a * a), 2):
        most = max((2 * n * a) % (a * a), most)
    runningCounter += most

print(runningCounter)
