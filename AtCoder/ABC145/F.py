N, K = map(int, input().split())
H = list(map(int, input().split()))

S = [0] + sorted(list(set(H)))
D = {h: i for i, h in enumerate(S)}


L = len(S)
K1 = K + 1
M = L * K1

dp = [1 << 60] * M
dp[0] = 0

for h in H:
    i = D[h]
    dp_next = [1 << 60] * M

    for m, v in enumerate(dp):
        j = m // K1
        k = m % K1

        i1 = i * K1 + k
        dp_next[i1] = min(dp_next[i1], v + max(0, h - S[j]))

        if k < K:
            i2 = m + 1
            dp_next[i2] = min(dp_next[i2], v)

    dp = dp_next

print(min(dp))
