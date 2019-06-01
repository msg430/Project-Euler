upperLimit = 100

counter = 0
for i in range(1, upperLimit+1):
    for j in range(i+1, upperLimit+1):
        counter += i*j

counter = 2*counter
print(counter)