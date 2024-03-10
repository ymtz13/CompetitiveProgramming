from collections import deque
from typing import List, Tuple


def isPrime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for p in range(3, x + 1):
        if p * p > x:
            break
        if x % p == 0:
            return False

    return True


def max_flow(N: int, S: int, T: int, edges: List[Tuple[int, int, int]]):
    """最大流問題を Ford-Fulkerson アルゴリズムで解く

    N (int): 頂点数

    S (int): 始点のインデックス

    T (int): 終点のインデックス

    edges: (辺の始点のインデックス, 辺の終点のインデックス, 辺の容量) のリスト
    """

    E = [[] for _ in range(N)]
    M = len(edges)
    M2 = M * 2

    EdgesFrom = [0] * M2
    EdgesTo = [0] * M2
    EdgesCap = [0] * M2

    for i, (f, t, cap) in enumerate(edges):
        j = i + M

        E[f].append(i)
        E[t].append(j)

        EdgesFrom[i] = EdgesTo[j] = f
        EdgesFrom[j] = EdgesTo[i] = t
        EdgesCap[i] = cap
        # EdgesCap[j] = cap # 無向辺の場合はアンコメントする

    visited = [-1] * N
    come_through = [-1] * N
    total_flow = 0

    for trial in range(1 << 60):
        queue = deque([S])
        while queue:
            q = queue.popleft()

            for iedge in E[q]:
                t = EdgesTo[iedge]
                cap = EdgesCap[iedge]

                if visited[t] == trial:
                    continue
                if cap == 0:
                    continue

                queue.append(t)
                visited[t] = trial
                come_through[t] = iedge

        if visited[T] != trial:
            break

        q = T
        path = []
        flow = 1 << 60
        while q != S:
            iedge = come_through[q]
            path.append(iedge)
            flow = min(flow, EdgesCap[iedge])
            q = EdgesFrom[iedge]

        for iedge in path:
            jedge = (iedge + M) % M2
            EdgesCap[iedge] -= flow
            EdgesCap[jedge] += flow

        total_flow += flow

    return total_flow


N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

I1 = None
B1 = 0

S = N
T = S + 1
edges = []

INF = 1 << 60

for i, (A, B) in enumerate(AB):
    if A == 1:
        I1 = i
        B1 = B
        continue

    if A % 2:
        edges.append((S, i, B))
    else:
        edges.append((i, T, B))

for i, (Ai, _) in enumerate(AB):
    for j, (Aj, _) in enumerate(AB):
        if Ai % 2 and Aj % 2 == 0 and isPrime(Ai + Aj):
            edges.append((i, j, INF))

base = max_flow(N + 2, S, T, edges)

edges.append(None)

ok = 0
ng = B1 + 1
while ng - ok > 1:
    tgt = (ng + ok) // 2
    edges[-1] = (S, I1, tgt)
    mf = max_flow(N + 2, S, T, edges)

    if mf == base + tgt:
        ok = tgt
    else:
        ng = tgt

r = B1 - ok
print(base + ok + r // 2)
