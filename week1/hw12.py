A = int(input())
B = int(input())
N = int(input())

cost1 = A * 100 + B
total_Cost = cost1 * N

print(total_Cost // 100, total_Cost % 100)
