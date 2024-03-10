N, M = map(int, input().split())
X = map(int, input().split())
X = [x - 1 for x in X]

A = [0] * (N + 1)

s = 0

for x0, x1 in zip(X, X[1:]):
    if x0 > x1:
        x0, x1 = x1, x0

    d = x1 - x0
    s += min(d, N - d)

    if d * 2 == N:
        continue

    if d * 2 < N:
        a = N - d * 2
        A[x0] += a
        A[x1] -= a
    else:
        a = d * 2 - N
        A[0] += a
        A[x0] -= a
        A[x1] += a
        A[N] -= a


V = []
v = 0
for a in A:
    v += a
    V.append(v)

print(s + min(V[:-1]))
