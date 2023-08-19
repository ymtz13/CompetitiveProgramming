from collections import deque

N1, N2, M = map(int, input().split())
E1 = [[] for _ in range(N1)]
E2 = [[] for _ in range(N2)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if a < N1:
        E1[a].append(b)
        E1[b].append(a)
    else:
        a -= N1
        b -= N1
        E2[a].append(b)
        E2[b].append(a)


def dfs(N, E, s):
    dist = [None] * N
    queue = deque([s])
    while queue:
        q = queue.popleft()
        d = q // N
        q = q % N
        if dist[q] is not None:
            continue
        dist[q] = d

        for e in E[q]:
            queue.append((d + 1) * N + e)

    return dist


D1 = dfs(N1, E1, 0)
D2 = dfs(N2, E2, N2 - 1)

print(max(D1) + max(D2) + 1)
