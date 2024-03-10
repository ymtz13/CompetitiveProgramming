N, S, M, L = map(int, input().split())

ans = 1 << 60
for nS in range(20):
    for nM in range(20):
        for nL in range(20):
            price = S * nS + M * nM + L * nL
            n = nS * 6 + nM * 8 + nL * 12
            if n >= N:
                ans = min(ans, price)

print(ans)
