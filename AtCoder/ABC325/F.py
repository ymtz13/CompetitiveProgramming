N = int(input())
D = list(map(int, input().split()))
L1, C1, K1 = map(int, input().split())
L2, C2, K2 = map(int, input().split())

dpK = [0] * (K1 + 1)

INF = 1 << 60

for d in D:
    X = []
    for n1 in range(K1 + 1):
        r = d - n1 * L1
        n2 = max(0, (r + L2 - 1) // L2)
        X.append(n2)

    dpK_next = [INF] * (K1 + 1)

    for n1L, n2L in enumerate(dpK):
        for n1, n2R in enumerate(X, n1L):
            if n1 > K1:
                break

            n2 = n2L + n2R
            dpK_next[n1] = min(dpK_next[n1], n2)

    dpK = dpK_next


ans = INF
for n1, n2 in enumerate(dpK):
    if n2 > K2:
        continue
    ans = min(ans, n1 * C1 + n2 * C2)

print(ans if ans < INF else -1)
