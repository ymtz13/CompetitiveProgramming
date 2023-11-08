from collections import deque

INF = 1 << 60

H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2
N = H2 * W2

M = []
M.append([INF] * W2)
for _ in range(H):
    M.append([INF] + list(map(int, input().split())) + [INF])
M.append([INF] * W2)

S = []

D = [0] * N
for h in range(1, H + 1):
    for w in range(1, W + 1):
        m = M[h][w]
        d = [
            m > M[h + 1][w],
            m > M[h - 1][w],
            m > M[h][w + 1],
            m > M[h][w - 1],
        ].count(True)

        i = h * W2 + w
        D[i] = d

        if d == 0:
            S.append(i)

ans = H * W


Z = [None] * N

for st in S:
    X = []
    queue = deque([st])
    while queue:
        q = queue.popleft()
        h = q // W2
        w = q % W2
        m = M[h][w]

        if m == INF:
            continue

        X.append((h, w))

        if M[h + 1][w] > m:
            qq = q + W2
            if Z[qq] is None or Z[qq] == st:
                Z[qq] = st
                D[qq] -= 1
                if D[qq] == 0:
                    queue.append(qq)

        if M[h - 1][w] > m:
            qq = q - W2
            if Z[qq] is None or Z[qq] == st:
                Z[qq] = st
                D[qq] -= 1
                if D[qq] == 0:
                    queue.append(qq)

        if M[h][w + 1] > m:
            qq = q + 1
            if Z[qq] is None or Z[qq] == st:
                Z[qq] = st
                D[qq] -= 1
                if D[qq] == 0:
                    queue.append(qq)

        if M[h][w - 1] > m:
            qq = q - 1
            if Z[qq] is None or Z[qq] == st:
                Z[qq] = st
                D[qq] -= 1
                if D[qq] == 0:
                    queue.append(qq)

    ans -= len(X)

print(ans)
