l1 = 109
v = int(input())
t = int(input())
a = (l1 + v * t % l1) % l1

print(a)
