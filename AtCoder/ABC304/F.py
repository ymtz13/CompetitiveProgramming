N = int(input())
S = [c == "." for c in input()]
Z = [0] * N

mod = 998244353

for p in range(1, N):
    if N % p:
        continue

    X = [0] * p
    for i, c in enumerate(S):
        if c:
            X[i % p] = 1

    cnt = X.count(0)
    Z[p] = pow(2, cnt, mod)

ans = 0
for i in range(1, N):
    if N % i:
        continue

    v = Z[i]
    ans += v
    ans %= mod
    # print(Z)

    for j in range(i * 2, N, i):
        Z[j] -= v
        Z[j] %= mod

print(ans)
