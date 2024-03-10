mod = 998244353

N = tuple(map(int, input()))
M = int(input())
C = tuple(map(int, input().split()))

L = len(N)

dpE = [0] * 1024
dpL = [0] * 1024
dsE = [0] * 1024
dsL = [0] * 1024

dpE[0] = 1

for i, n in enumerate(N):
    dpE_next = [0] * 1024
    dpL_next = [0] * 1024
    dsE_next = [0] * 1024
    dsL_next = [0] * 1024
    dpL_next[0] = 1

    i = pow(10, L - i - 1, mod)

    for v in range(10):
        b = 1 << v

        if v < n:
            for f in range(0 if v else 1, 1024):
                t = f | b
                c = dpL[f] + dpE[f]
                dpL_next[t] += c
                dsL_next[t] += dsL[f] + dsE[f] + c * v * i
                dpL_next[t] %= mod
                dsL_next[t] %= mod

        if v == n:
            for f in range(0 if v else 1, 1024):
                t = f | b
                dpL_next[t] += dpL[f]
                dsL_next[t] += dsL[f] + dpL[f] * v * i
                dpL_next[t] %= mod
                dsL_next[t] %= mod
                dpE_next[t] += dpE[f]
                dsE_next[t] += dsE[f] + dpE[f] * v * i
                dpE_next[t] %= mod
                dsE_next[t] %= mod

        if v > n:
            for f in range(1024):
                t = f | b
                dpL_next[t] += dpL[f]
                dsL_next[t] += dsL[f] + dpL[f] * v * i
                dpL_next[t] %= mod
                dsL_next[t] %= mod

    dpE = dpE_next
    dpL = dpL_next
    dsE = dsE_next
    dsL = dsL_next


K = sum(1 << c for c in C)


ans = 0
for b, (vE, vL) in enumerate(zip(dsE, dsL)):
    if b & K == K:
        ans += vE + vL
        ans %= mod

print(ans)
