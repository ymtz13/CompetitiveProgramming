N = int(input())
p = 0
for i in range(N):
    x, u = input().split()
    p += int(x) if u=='JPY' else float(x)*380000
print(p)
