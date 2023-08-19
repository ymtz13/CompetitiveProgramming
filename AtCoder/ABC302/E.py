N, Q = map(int, input().split())
E = [set() for _ in range(N + 1)]
ans = []
cnt = N

for _ in range(Q):
    query = tuple(map(int, input().split()))
    t = query[0]

    if t == 1:
        _, u, v = query
        E[u].add(v)
        E[v].add(u)
        if len(E[u]) == 1:
            cnt -= 1
        if len(E[v]) == 1:
            cnt -= 1

    if t == 2:
        _, v = query
        for u in E[v]:
            eu = E[u]
            eu.remove(v)
            if len(eu) == 0:
                cnt += 1

        if len(E[v]) > 0:
            cnt += 1
        E[v].clear()

    ans.append(cnt)


for a in ans:
    print(a)
