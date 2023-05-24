N = int(input())

H = N // 3600 % 12
M = N // 60 % 60
S = N % 3600
M = (len(str(M)) % 2) * '0' + str(M)
S = (len(str(S)) % 2) * '0' + str(S)
print(H, ':', M, ':', S, sep='')
