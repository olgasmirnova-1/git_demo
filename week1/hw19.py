H1 = int(input())
M1 = int(input())
S1 = int(input())

H2 = int(input())
M2 = int(input())
S2 = int(input())

T1 = (H1 * 3600) + (M1 * 60) + S1
T2 = (H2 * 3600) + (M2 * 60) + S2

T = T2 - T1
print(T)
