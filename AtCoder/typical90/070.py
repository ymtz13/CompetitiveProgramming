N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
X = sorted([x for x, y in P])
Y = sorted([y for x, y in P])

Px = X[N//2]
Py = Y[N//2]

ans = sum([abs(x-Px) for x in X]) + sum([abs(y-Py) for y in Y])
print(ans)
