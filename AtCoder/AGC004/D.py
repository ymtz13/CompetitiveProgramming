from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

E = [[] for _ in range(N)]
for i, a in enumerate(A[1:], 1):
    E[a - 1].append(i)


queue = deque([0])
V = []
while queue:
    q = queue.popleft()
    V.append(q)

    for e in E[q]:
        queue.append(e)

D = [-1] * N
ans = 0
for v in reversed(V):
    d = 0
    for e in E[v]:
        d = max(d, D[e] + 1)
    D[v] = d

    if v != 0 and d % K == K - 1 and A[v] != 1:
        ans += 1
        D[v] = -1


if A[0] != 1:
    ans += 1

print(ans)
