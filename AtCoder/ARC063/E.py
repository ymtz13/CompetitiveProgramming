from collections import deque

INF = 1 << 60


def no():
    print("No")
    exit()


N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    E[A - 1].append(B - 1)
    E[B - 1].append(A - 1)

ans = [None] * N
X = [None] * N
Z = [False] * N
K = int(input())
for _ in range(K):
    V, P = map(int, input().split())
    ans[V - 1] = P
    X[V - 1] = (P, P)
    Z[V - 1] = True

for q in range(N):
    for e in E[q]:
        xq = X[q]
        xe = X[e]
        if xq and xe:
            xqL = xq[0]
            xeL = xe[0]
            if abs(xqL - xeL) != 1:
                no()

visited = [False] * N
dist = [None] * N
parent = [None] * N

for st in range(N):
    if visited[st] or Z[st]:
        continue

    tree = []

    queue = deque([st])
    while queue:
        q = queue.popleft()
        d, q = q // N, q % N
        if visited[q]:
            continue
        tree.append(d * N + q)
        dist[q] = d

        if X[q] is None:
            visited[q] = True

            for e in E[q]:
                queue.append((d + 1) * N + e)

    tree.sort()
    # print([t % N for t in tree])

    for q in reversed(tree):
        d, q = q // N, q % N
        if Z[q]:
            continue

        x = None
        for e in E[q]:
            if dist[e] < d:
                parent[q] = e
                continue
            xe = X[e]
            # print(q, e, xe)

            if xe:
                eL, eR = xe
                vL = eL - 1
                vR = eR + 1

                if x:
                    xL, xR = x
                    if xL % 2 != vL % 2:
                        no()
                    else:
                        x = (max(xL, vL), min(xR, vR))
                        if x[0] > x[1]:
                            no()
                else:
                    x = (vL, vR)

        X[q] = x

    # print(X)
    # print(dist, "<-dist")
    # print(parent)

    for q in tree:
        q = q % N
        p = parent[q]
        x = X[q]

        if p is None:
            # print(q)
            ans[q] = x[0]
        else:
            ap = ans[p]
            ans[q] = ap + 1 if x and ap - 1 < x[0] else ap - 1


# print(X)
# print(ans)

print("Yes")
for a in ans:
    print(a)

# 1-2
# +-3-4
#   +-5

# 0(5,7)-1(6)
# +-2(6,8)-3
#   +-4(7)
