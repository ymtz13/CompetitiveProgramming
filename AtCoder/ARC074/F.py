from collections import deque
from typing import List, Tuple


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
        EdgesCap[j] = cap

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


H, W = map(int, input().split())

N = H + W
E = []

INF = N + 5

for h in range(H):
    for w, c in enumerate(input(), H):
        if c == "o":
            E.append((h, w, 1))
        if c in "ST":
            E.append((h, w, INF))

            if c == "S":
                s = h
            else:
                t = h

if s == t:
    print(-1)
    exit()

mf = max_flow(N, s, t, E)

print(mf if mf < INF else -1)
