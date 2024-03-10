from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

queue = deque([])
start = [None] * N
color = [None] * N

ntot = ndot = nbip = 0
for st in range(N):
    if start[st] is not None:
        continue

    dot = True
    bip = True
    queue = deque([(st, 0)])
    while queue:
        q, c = queue.popleft()
        if start[q] is not None:
            if start[q] == st and color[q] != c:
                bip = False
            continue
        start[q] = st
        color[q] = c

        if q != st:
            dot = False

        for e in E[q]:
            queue.append((e, 1 - c))

    ntot += 1
    if dot:
        ndot += 1
    elif bip:
        nbip += 1


nn = ntot - ndot
ans = nn * nn + nbip * nbip + ndot * N * 2 - ndot * ndot
print(ans)
