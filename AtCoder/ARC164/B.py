from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

C = list(map(int, input().split()))

visited = [False] * N
ok = False

for st in range(N):
    if ok:
        break
    if visited[st]:
        continue
    queue = deque([(st, None)])
    S = set()

    while queue and not ok:
        q, par = queue.popleft()
        if visited[q]:
            continue
        visited[q] = True
        S.add(q)

        cq = C[q]

        for e in E[q]:
            if e == par:
                continue

            ce = C[e]
            if cq == ce:
                if e in S:
                    ok = True
                    break
            else:
                queue.append((e, q))

print("Yes" if ok else "No")
