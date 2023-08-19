from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)

K = int(input())
PD = [tuple(map(int, input().split())) for _ in range(K)]

isBlack = [1] * N
LL = []
for p, D in PD:
    visited = [False] * N
    queue = deque([(0, p - 1)])
    L = []
    LL.append(L)
    while queue:
        d, q = queue.popleft()
        if visited[q]:
            continue
        visited[q] = True

        if d == D:
            L.append(q)
            continue

        isBlack[q] = 0
        for e in E[q]:
            queue.append((d + 1, e))

# print(LL)

ok = all([any([isBlack[x] for x in L]) for L in LL])
if not ok:
    print("No")
    exit()

print("Yes")
print(*isBlack, sep="")
