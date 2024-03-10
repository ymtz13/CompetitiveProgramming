from itertools import permutations, product

N, M, K = map(int, input().split())

E = [[-1] * N for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    E[u][v] = E[v][u] = w

P = list(permutations(range(1, N)))
Parents = list(product(*[range(n) for n in range(1, N)]))

ans = INF = 1 << 60


for nodes in P:
    nodes = (0,) + nodes
    for parents in Parents:
        v = 0
        for iq, ip in enumerate(parents, 1):
            nodeq = nodes[iq]
            nodep = nodes[ip]

            w = E[nodeq][nodep]

            if w == -1:
                v = INF
                break

            v += w
            v %= K

        ans = min(ans, v)

print(ans)
