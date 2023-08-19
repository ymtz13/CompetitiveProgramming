N = int(input())

G = [[[None] * 100 for _ in range(100)] for _ in range(100)]

for i in range(1, N + 1):
    X1, Y1, Z1, X2, Y2, Z2 = map(int, input().split())

    for x in range(X1, X2):
        for y in range(Y1, Y2):
            for z in range(Z1, Z2):
                G[x][y][z] = i

ans = [set() for _ in range(N + 1)]

for x in range(100):
    for y in range(100):
        for z in range(100):
            v = G[x][y][z]
            if not v:
                continue

            if x > 0:
                w = G[x - 1][y][z]
                if w and w != v:
                    ans[v].add(w)
                    ans[w].add(v)

            if y > 0:
                w = G[x][y - 1][z]
                if w and w != v:
                    ans[v].add(w)
                    ans[w].add(v)

            if z > 0:
                w = G[x][y][z - 1]
                if w and w != v:
                    ans[v].add(w)
                    ans[w].add(v)

for a in ans[1:]:
    print(len(a))
