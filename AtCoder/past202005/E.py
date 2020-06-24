N, M, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    E[u-1].append(v-1)
    E[v-1].append(u-1)

color = list(map(int, input().split()))

for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0]==1:
        x = query[1]
        cx = color[x-1]
        print(cx)
        for y in E[x-1]:
            color[y] = cx

    else:
        _, x, y = query
        print(color[x-1])
        color[x-1] = y
