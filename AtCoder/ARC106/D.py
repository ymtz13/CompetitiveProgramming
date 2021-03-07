N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353

S = [0]*(K+1)
for a in A:
    v = 1
    for x in range(K+1):
        S[x] = (S[x]+v)%mod
        v = v*a%mod

B = [[0]*(K+1) for _ in range(K+1)]
for n in range(K+1):
    B[n][0] = B[n][n] = 1
    for k in range(1, n):
        B[n][k] = (B[n-1][k]+B[n-1][k-1]) % mod

inv2 = pow(2, mod-2, mod)

for X in range(1, K+1):
    s = 0
    for p in range(X+1):
        b = B[X][p]
        s = (s + S[p]*S[X-p]*b)%mod

    diag = pow(2, X, mod)*S[X]%mod
    ans = (s-diag)*inv2%mod
    print(ans)