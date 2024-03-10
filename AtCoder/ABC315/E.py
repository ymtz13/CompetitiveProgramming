from collections import deque

N = int(input())
P = [None] + [tuple(map(int, input().split()))[1:] for _ in range(N)]

queue = deque([1])

X = []
while queue:
    q = queue.popleft()
    X.append(q)

    for p in P[q]:
        queue.append(p)

s = set()
ans = []
for x in reversed(X):
    if x not in s:
        ans.append(x)
        s.add(x)


print(*ans[:-1])
