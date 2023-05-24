a = int(input())
b = int(input())
c = int(input())
d = int(input())

cost1 = a * 100 + b
cost2 = c * 100 + d
total_Cost = cost1 + cost2

print(total_Cost // 100, total_Cost % 100)