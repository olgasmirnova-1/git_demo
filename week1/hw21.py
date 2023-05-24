import math
H = int(input())
A = int(input())
B = int(input())
C = A - B


D = (H - A) // (A - B) + 1

print(math.ceil(D))
