mod = 998244353

N = int(input())
A = list(map(int, input().split()))

Ninv = pow(N, mod - 2, mod)

s = 1
ans = 0

for a in A:
    p = s * Ninv
    p %= mod

    s += p
    s %= mod

    ans += a * p
    ans %= mod

print(ans)
