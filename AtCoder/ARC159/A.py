from collections import deque

N, K = map(int, input().split())
E = []
for _ in range(N):
    A = tuple(map(int, input().split()))
    E.append([i for i, a in enumerate(A) if a])


ans = []
Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s = (s - 1) % N
    t = (t - 1) % N

    queue = deque([(s, 0)])
    dist = [None] * N
    while queue:
        q, d = queue.popleft()
        if dist[q] is not None:
            continue
        if d > 0:
            dist[q] = d

        for e in E[q]:
            queue.append((e, d + 1))

    ans.append(dist[t])

for a in ans:
    print(a if a is not None else -1)
