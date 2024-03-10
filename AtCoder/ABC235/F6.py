mod = 998244353

N = tuple(map(int, input()))
M = int(input())
C = tuple(map(int, input().split()))

dpE = [0] * 1024
dpL = [0] * 1024

dpE[0] = 1

for n in N:
    dpE_next = [0] * 1024
    dpL_next = [0] * 1024
    dpL_next[0] = 1

    for v in range(10):
        b = 1 << v

        if v < n:
            for f in range(0 if v else 1, 1024):
                t = f | b
                dpL_next[t] += dpL[f] + dpE[f]
                dpL_next[t] %= mod

        if v == n:
            for f in range(0 if v else 1, 1024):
                t = f | b
                dpL_next[t] += dpL[f]
                dpL_next[t] %= mod
                dpE_next[t] += dpE[f]
                dpE_next[t] %= mod

        if v > n:
            for f in range(1024):
                t = f | b
                dpL_next[t] += dpL[f]
                dpL_next[t] %= mod

    dpE = dpE_next
    dpL = dpL_next

K = sum(1 << c for c in C)

ans = 0
for b, (vE, vL) in enumerate(zip(dpE, dpL)):
    if b & K == K:
        ans += vE + vL
        ans %= mod

print(ans)
