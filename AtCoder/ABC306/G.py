from collections import deque
from math import gcd

T = int(input())

ans = []

for _ in range(T):
    N, M = map(int, input().split())

    E0 = [[] for _ in range(N)]
    E1 = [[] for _ in range(N)]
    for _ in range(M):
        U, V = map(int, input().split())
        U -= 1
        V -= 1
        E0[U].append(V)
        E1[V].append(U)

    queue = deque([0])
    dist0 = [None] * N
    while queue:
        q = queue.popleft()
        d = q // N
        q = q % N
        if dist0[q] is not None:
            continue
        dist0[q] = d

        for e in E0[q]:
            queue.append((d + 1) * N + e)

    queue = deque([0])
    dist1 = [None] * N
    while queue:
        q = queue.popleft()
        d = q // N
        q = q % N
        if dist1[q] is not None:
            continue
        dist1[q] = d

        for e in E1[q]:
            queue.append((d + 1) * N + e)

    L = []
    for d0, d1 in zip(dist0[1:], dist1[1:]):
        if d0 is None or d1 is None:
            continue
        L.append(d0 + d1)

    if not L:
        ans.append("No")
        continue

    g = L[0]
    for v in L:
        g = gcd(g, v)

    while g % 2 == 0:
        g //= 2
    while g % 5 == 0:
        g //= 5

    ans.append("Yes" if g == 1 else "No")


for a in ans:
    print(a)
