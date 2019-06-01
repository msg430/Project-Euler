counter = 0
limit = 1000

for i in range(1, limit):
    if i % 3 == 0 or i % 5 == 0:
       # print ("adding", i, "to", counter)
        counter = counter + i

print(counter)
