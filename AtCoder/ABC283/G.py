N, L, R = map(int, input().split())
A = list(map(int, input().split()))

X = []
for j in range(61, -1, -1):
    if not A:
        break

    pj = 1 << j

    A.sort(reverse=True)
    if A[0] & pj:
        x = A[0]
        X.append((x, pj))
        A = [a ^ x if a & pj else a for a in A[1:]]

for i, (x, pj) in enumerate(X):
    for k, (xk, pk) in enumerate(X[:i]):
        if xk & pj:
            X[k] = (xk ^ x, pk)

X.reverse()

ans = []
for v in range(L - 1, R):
    z = 0
    for i, (x, _) in enumerate(X):
        if (v >> i) & 1:
            z ^= x
    ans.append(z)


print(*ans)
