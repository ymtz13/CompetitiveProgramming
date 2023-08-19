from collections import deque

N = int(input())
E = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

ALL = N * (N - 1) * (N - 2) // 6

queue = deque([(0, None)])
parent = [None] * N
l = []

while queue:
    q, p = queue.popleft()
    l.append(q)
    parent[q] = p

    for e in E[q]:
        if e == p:
            continue
        queue.append((e, q))

C = [0] * N

for q in reversed(l):
    c = 1
    for e in E[q]:
        if e == parent[q]:
            continue
        c += C[e]
    C[q] = c

# print(C)

s = 0
for i in range(N):
    X = []
    for e in E[i]:
        if e == parent[i]:
            continue
        X.append(C[e])

    X.append(N - 1 - sum(X))

    S = sum(X)
    S2 = S * S
    for x in X:
        S2 -= x * x

    # print(i + 1, X, S2)

    s += S2 // 2

print(ALL - s)
