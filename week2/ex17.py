A, B, C = int(input()), int(input()), int(input())
D, E = int(input()), int(input())

if A <= D and B <= E or A <= E and B <= D:
    print('YES')
elif C <= D and B <= E or C <= E and B <= D:
    print('YES')
elif A <= D and C <= E or A <= E and C <= D:
    print('YES')
else:
    print('NO')
