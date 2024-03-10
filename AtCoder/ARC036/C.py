N, K = map(int, input().split())
S = input()

M = N + 10
offsetMax = 1
offsetMin = N + 5

dp = [[0] * M for _ in range(M)]
dp[offsetMax][offsetMin] = 1

mod = 10**9 + 7

for c in S:
    dp_next = [[0] * M for _ in range(M)]

    for fMax in range(-1, N + 1):
        for fMin in range(-N, 2):
            v = dp[fMax + offsetMax][fMin + offsetMin]

            if c in "0?":
                tMax = fMax + 1 if fMax >= 0 else 1
                tMin = fMin + 1 if fMin <= 0 else 1
                if tMax <= K:
                    dp_next[tMax + offsetMax][tMin + offsetMin] += v
                    dp_next[tMax + offsetMax][tMin + offsetMin] %= mod

            if c in "1?":
                tMax = fMax - 1 if fMax >= 0 else -1
                tMin = fMin - 1 if fMin <= 0 else -1
                if tMin >= -K:
                    dp_next[tMax + offsetMax][tMin + offsetMin] += v
                    dp_next[tMax + offsetMax][tMin + offsetMin] %= mod

    dp = dp_next

    # print(c)
    # for fMax, row in enumerate(dp):
    #     for fMin, v in enumerate(row):
    #         if v:
    #             print((fMax - offsetMax, fMin - offsetMin), v)

ans = 0
for row in dp:
    for v in row:
        ans += v
        ans %= mod

print(ans)
