Y = int(input())
a = Y % 400
b = Y % 100
c = Y % 4
if a == 0:
    print('YES')
elif b == 0:
    print('NO')
elif c == 0:
    print('YES')
else:
    print('NO')
