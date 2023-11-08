from collections import deque


def max_flow(N, S, T, edges):
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


N, M = map(int, input().split())
C = list(map(int, input().split()))
A = list(map(int, input().split()))
L = [tuple(map(int, input().split())) for _ in range(M)]

offset = sum(A)

# S                       : 0
# T                       : 1
# Archievement[i = 0..M]  : i+2
# Skill[j = 0..N, lv=2..6]: M+j*4+lv

# S           , Archievement[i], A[i]
# Skill[j][lv], T              , C[j]
# Skill[j][lv], Skill[j][lv-1] , INF

edges = []

INF = 1 << 60
S = 0
T = 1
Archievements = [i + 2 for i in range(M)]
Skills = [[M + j * 4 + lv for lv in range(6)] for j in range(N)]

for i, a in enumerate(A):
    edges.append((S, i + 2, a))

for j, c in enumerate(C):
    for lv in range(2, 6):
        edges.append((Skills[j][lv], T, c))

    for lv in range(3, 6):
        edges.append((Skills[j][lv], Skills[j][lv - 1], INF))

for i, l in enumerate(L):
    for j, lv in enumerate(l):
        if lv >= 2:
            edges.append((Archievements[i], Skills[j][lv], INF))

maxflow = max_flow(2 + N * 4 + M, S, T, edges)

print(offset - maxflow)
