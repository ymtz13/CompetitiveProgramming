from collections import deque

N = int(input())
M = int(input())
E = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    E[A].append(B)
    E[B].append(A)

queue = deque([(1, 0)])
dist = [9] * (N + 1)

while queue:
    q, d = queue.popleft()
    if dist[q] != 9:
        continue
    dist[q] = d

    if d <= 1:
        for e in E[q]:
            queue.append((e, d + 1))

print(len([d for d in dist if 1 <= d <= 2]))
