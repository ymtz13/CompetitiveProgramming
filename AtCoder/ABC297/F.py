mod = 998244353

M = 2 * 10**6
F = [1]
for i in range(1, M):
    F.append(F[-1] * i % mod)

Finv = [None] * (M)
Finv[-1] = pow(F[-1], mod - 2, mod)

for i in range(M - 2, -1, -1):
    Finv[i] = Finv[i + 1] * (i + 1) % mod


def comb(n, k):
    return F[n] * Finv[n - k] * Finv[k] % mod


H, W, K = map(int, input().split())

Z = comb(H * W, K)
Zinv = pow(Z, mod - 2, mod)

S = [[0] * (W + 1) for _ in range(H + 1)]
ans = 0

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if h * w < K:
            continue

        cH = H - h + 1
        cW = W - w + 1
        c = cH * cW

        x = comb(h * w, K) - S[h - 1][w] * 2 - S[h][w - 1] * 2 + S[h - 1][w - 1] * 4
        if h > 1:
            x += S[h - 2][w] - S[h - 2][w - 1] * 2
        if w > 1:
            x += S[h][w - 2] - S[h - 1][w - 2] * 2
        if h > 1 and w > 1:
            x += S[h - 2][w - 2]

        S[h][w] = x

        ans += c * h * w * x * Zinv % mod
        ans %= mod

print(ans)
