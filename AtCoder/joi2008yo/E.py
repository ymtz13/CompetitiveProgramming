R, C = map(int, input().split())
V = [0] * C

n = 1
for _ in range(R):
    A = list(map(int, input().split()))
    for i, a in enumerate(A):
        V[i] += n * a
    n *= 2

popcount = [0] * (1 << R)
for z in range(1 << R):
    n = 0
    for i in range(R):
        n += (z >> i) & 1
    popcount[z] = n

ans = 0
for z in range(1 << R):
    P = [popcount[z ^ v] for v in V]
    ans = max(ans, sum([max(p, R - p) for p in P]))

print(ans)
