limit = 4000000

counter = 0
first = 1
second = 2
while second < limit:
    counter += second
    holder = second+first
    first = 2*second+first
    second = holder+first

print(counter)