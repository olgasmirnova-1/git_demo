x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())

X = x - x2
Y = y - y2

if X in (1, -1, 0) and Y in (1, -1, 0):
    print("YES")
else:
    print("NO")
