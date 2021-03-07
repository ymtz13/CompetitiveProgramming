N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

P = [K]
for i in range(31):
    b = 1<<i
    if K&b: P.append((K-b)|(b-1))

ans = 0
for p in P:
    s = 0
    for a, b in AB:
        if a&(~p): continue
        s += b
    ans = max(ans, s)

print(ans)
