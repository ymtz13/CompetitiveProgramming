from itertools import permutations

INF = 1 << 60

N, M = map(int, input().split())

E = [[-INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    E[A][B] = E[B][A] = C

ans = 0

for perm in permutations(range(1, N + 1)):
    d = 0
    s = perm[0]
    for t in perm[1:]:
        d += E[s][t]
        ans = max(ans, d)
        s = t


print(ans)
