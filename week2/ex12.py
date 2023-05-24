x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 >= x1 and y2 >= y1 and (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")
