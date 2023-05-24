now = int(input())
numMax = now
while now != 0:
    now = int(input())
    if now != 0 and now > numMax:
        numMax = now
print(numMax)
