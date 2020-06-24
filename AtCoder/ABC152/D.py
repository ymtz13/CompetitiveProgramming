N = int(input())
X = [[0]*10 for _ in range(10)]
for n in range(1, N+1):
    s = str(n)
    a = int(s[0])
    b = int(s[-1])
    X[a][b] += 1

ans = 0
for a in range(1,10):
    for b in range(1,10):
        ans += X[a][b]*X[b][a]
print(ans)
