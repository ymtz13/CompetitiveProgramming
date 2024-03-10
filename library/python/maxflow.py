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

    # 残余グラフ上でSから到達可能な頂点集合
    reachable = [t for t in range(N) if visited[t] == trial]

    return (total_flow, reachable)


# 0 --[2]-> 1 --[5]-> 2
# |                   ^
# |--------[6]--------|

flow = max_flow(
    4,
    0,
    2,
    [
        (0, 1, 2),
        (1, 2, 5),
        (0, 2, 6),
    ],
)

assert flow == 8
