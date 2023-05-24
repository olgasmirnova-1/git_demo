N = int(input())
i = 1
minNum = 1
while i <= N:
    i = i + 1
    if N % i == 0:
        print(i)
    break
