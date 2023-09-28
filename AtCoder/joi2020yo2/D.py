# 7 8 9
# 4 5 6
# 1 2 3
# 0

D = [
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    [0, 1, 2, 3, 2, 3, 4, 3, 4, 5],
    [1, 0, 1, 2, 1, 2, 3, 2, 3, 4],
    [2, 1, 0, 1, 2, 1, 2, 3, 2, 3],
    [3, 2, 1, 0, 3, 2, 1, 4, 3, 2],
    [2, 1, 2, 3, 0, 1, 2, 1, 2, 3],
    [3, 2, 1, 2, 1, 0, 1, 2, 1, 2],
    [4, 3, 2, 1, 2, 1, 0, 3, 2, 1],
    [3, 2, 3, 4, 1, 2, 3, 0, 1, 2],
    [4, 3, 2, 3, 2, 1, 2, 1, 0, 1],
    [5, 4, 3, 2, 3, 2, 1, 2, 1, 0],
]
D = [[d + 1 for d in row] for row in D]

INF = 100


M, R = map(int, input().split())
N = M * 10
dp = [INF] * N
dp[0] = 0


for n in range(30):
    dp_next = dp[:]
    for i, v in enumerate(dp):
        if v >= INF:
            continue

        r = i // 10
        d = i % 10
        for dd, dist in enumerate(D[d]):
            rr = (r * 10 + dd) % M
            j = rr * 10 + dd
            dp_next[j] = min(dp_next[j], v + dist)

    dp = dp_next

print(min(dp[R * 10 : (R + 1) * 10]))
