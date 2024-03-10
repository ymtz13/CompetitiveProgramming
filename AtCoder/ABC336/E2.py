M = 200

DP = [[0] * (M * 2)]
DP[0][0] = 1
for _ in range(15):
    dp = DP[-1]
    dp_next = [0] * len(dp)

    for m in range(M):
        for d in range(10):
            dp_next[m + d] += dp[m]

    DP.append(dp_next)

print(DP[0][:50])
print(DP[1][:50])
print(DP[2][:50])


N = int(input())
N1 = N + 1

D = []
v = N1
while v:
    D.append(v % 10)
    v //= 10

D.reverse()
# print(D)

C = [0] * M

for i, d in enumerate(D):
    if d == 0:
        continue

    n = len(D) - i - 1
    s = sum(D[: i + 1]) - 1

    # print(i, n, s)

    for m, v in enumerate(DP[n][: M - s]):
        C[m + s] += v

    # print(C[:20])
