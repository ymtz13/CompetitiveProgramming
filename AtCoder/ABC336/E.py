M = 150

N = int(input())
N1 = N + 1

D = []
v = N1
while v:
    D.append(v % 10)
    v //= 10

D.reverse()

ans = [0] * M

for p, d in enumerate(D):
    if d == 0:
        continue

    for m in range(1, M):
        m1 = m + 1
        mm1 = m1 * m

        dp = [0] * mm1
        dp[0] = 1
        for q in range(len(D)):
            dp_next = [0] * mm1

            k = pow(10, len(D) - q - 1, m)

            if q < p:
                A = [D[q]]
            if q == p:
                A = range(D[q])
            if q > p:
                A = range(10)

            for i, v in enumerate(dp):
                t = i // m
                mod = i % m

                for dd in A:
                    j = (t + dd) * m + ((mod + dd * k) % m)
                    if j < mm1:
                        dp_next[j] += dp[i]

            dp = dp_next

        v = dp[m * m]
        ans[m] += v


print(sum(ans))
