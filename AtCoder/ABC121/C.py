N, M = list(map(int, input().split()))
AB = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:x[0])

m, p = 0, 0
for a, b in AB:
    if m+b>=M:
        p += (M-m)*a
        break
    m += b
    p += b*a

print(p)
