from collections import deque

M = 1000010
T = []
for i in range(M):
    s = sum(map(int, str(i)))
    T.append(i + s)

F = [[] for _ in range(M)]
for i, t in enumerate(T):
    if t < M:
        F[t].append(i)


N = int(input())
queue = deque([N])

ans = set()
while queue:
    q = queue.popleft()
    if q in ans:
        continue

    ans.add(q)
    for f in F[q]:
        queue.append(f)

print(len(ans))
