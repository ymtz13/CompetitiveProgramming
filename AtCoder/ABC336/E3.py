M = 150

N = int(input())
N1 = N + 1

D = []
v = N1
while v:
    D.append(v % 10)
    v //= 10

D.reverse()
# print(D)

ans = [0] * M

p = 0

for i, d in enumerate(D):
    if d == 0:
        continue

    p = (d - 1) * 10 ** (len(D) - i - 1)
    for ii, dd in enumerate(D[:i]):
        p += dd * 10 ** (len(D) - ii - 1)
    print(p)

    n = len(D) - i - 1
    s = sum(D[: i + 1]) - 1

    for m in range(max(1, s), M):
        T = m - s
        T1 = T + 1
        T1m = T1 * m

        dp = [0] * T1m
        dp[0] = 1
        for _ in range(n):
            dp_next = [0] * T1m

            for i, v in enumerate(dp):
                t = i // m
                mod = i % m

                for d in range(10):
                    j = (t + d) * m + ((mod + d) % m)
                    if j < T1m:
                        dp_next[j] += dp[i]

            dp = dp_next

        mod = (-p) % m

        v = dp[T * m + mod]
        ans[m] += v
        print(m, v)

print(sum(ans))
