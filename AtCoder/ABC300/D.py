M = 1000000
X = [True] * M
P = []
for p in range(2, M):
    if not X[p]:
        continue
    P.append(p)
    for i in range(p * 2, M, p):
        X[i] = False


N = int(input())

ans = 0
for c in P:
    c2 = c * c
    for b in P:
        if b >= c or b * c2 > N:
            break
        for a in P:
            if a >= b or a * a * b * c2 > N:
                break
            ans += 1

print(ans)
