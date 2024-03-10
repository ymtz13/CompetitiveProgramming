K, Q = map(int, input().split())
D = list(map(int, input().split()))
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

for N, X, M in Queries:
    DD = [d % M if d % M > 0 else M for d in D]

    S = X
    for i, dd in enumerate(DD):
        S += dd * ((N + K - i - 2) // K)

    print((N - 1) - (S // M - X // M))

# X   D[0] D[1] D[2] D[3]
# 3 + 3   + 1   + 4   + 3
# 3   6     7     11    14
# 1   0     1      1     0
# 3 ~ 14
