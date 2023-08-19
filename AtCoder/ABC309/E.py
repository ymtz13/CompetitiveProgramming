from collections import deque

N, M = map(int, input().split())
P = list(map(int, input().split()))

C = [[] for _ in range(N)]
for i, p in enumerate(P, 1):
    C[p - 1].append(i)

P = [None] + [p - 1 for p in P]

Y = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    Y[x - 1] = max(Y[x - 1], y + 1)


queue = deque([0])
while queue:
    q = queue.popleft()
    p = P[q]

    if p is not None and Y[p]:
        Y[q] = max(Y[q], Y[p] - 1)

    for c in C[q]:
        queue.append(c)

ans = 0
for y in Y:
    if y:
        ans += 1

print(ans)
