from collections import deque


def f(L):
    M = L // 2
    P0 = 1 if L % 2 == 0 else 2
    P = [P0 + 2 * i for i in range(M)]

    S = sum(P)

    q = S
    Q = []
    for p in P:
        if q <= 200000:
            Q.append(q)
        q -= p

    return Q


N, L = map(int, input().split())
M = 200001

E = f(L)
dist = [-1] * M
queue = deque([0])
while queue:
    q = queue.popleft()
    d = q // M
    q = q % M
    if dist[q] != -1:
        continue
    dist[q] = d

    for e in E:
        r = q + e
        if r < M:
            queue.append((d + 1) * M + r)


A = list(map(int, input().split()))
for a in A:
    print(dist[a])
