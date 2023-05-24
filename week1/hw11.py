N = int(input())
N1 = N % (24 * 60)
R1 = N1 // 60
R2 = N1 % 60
print(R1, R2)
