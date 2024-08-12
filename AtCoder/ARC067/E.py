mod = 10**9 + 7

F = [1]
for i in range(1, 2000):
    F.append(F[-1] * i % mod)

Finv = [pow(f, mod - 2, mod) for f in F]

N, A, B, C, D = map(int, input().split())

dp = [0] * (N + 1)
dp[0] = 1

for m in range(A, B + 1):
    for i in range(N, 0, -1):
        for k in range(C, D + 1):
            t = m * k
            j = i - t
            if j < 0:
                break
            if dp[j] == 0:
                continue

            n = N - j
            p = F[n] * Finv[n - t] * pow(Finv[m], k, mod) % mod
            h = p * Finv[k] % mod

            # print(m, j, i, f"k:{k}, n:{n}, p:{p}, h:{h}")

            dp[i] += dp[j] * h % mod
            dp[i] %= mod

print(dp[-1])
