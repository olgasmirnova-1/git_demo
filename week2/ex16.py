A1, B1, C1, A2, B2, C2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
if A1 * C1 == A2 * B2 and B1 * C1 == B2 * C2:
    print('Boxes are equal')
elif A1 * C1 > A2 * B2 and B1 * C1 > B2 * C2:
    print('The first box is larger than the second one')
elif A1 * C1 < A2 * B2 and B1 * C1 < B2 * C2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
