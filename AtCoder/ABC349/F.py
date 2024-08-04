mod = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))

MM = M

f = {}

c = 0
while MM % 2 == 0:
    MM //= 2
    c += 1
if c:
    f[2] = c

for p in range(3, M + 1, 2):
    if p * p > MM:
        break

    c = 0
    while MM % p == 0:
        MM //= p
        c += 1
    if c:
        f[p] = c


if MM > 1:
    f[MM] = 1


ff = [pow(p, v) for p, v in f.items()]

K = len(f)

nfree = 0
X = [0] * (1 << K)
for a in A:
    if M % a:
        continue

    x = 0
    for i, z in enumerate(ff):
        if a % z == 0:
            x += 1 << i
    X[x] += 1

dp = [0] * (1 << K)
dp[0] = 1
for x, c in enumerate(X):
    if c == 0:
        continue
    p = pow(2, c, mod) - 1
    for f in range((1 << K) - 1, -1, -1):
        t = f | x
        dp[t] += dp[f] * p
        dp[t] %= mod

ans = dp[-1]
if M == 1:
    ans -= 1

print(ans)
