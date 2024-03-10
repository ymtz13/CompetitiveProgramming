N, Q = map(int, input().split())
C = [{c} for c in map(int, input().split())]

Queries = [tuple(map(int, input().split())) for _ in range(Q)]

empty = set()

for f, t in Queries:
    f -= 1
    t -= 1

    cf = C[f]
    ct = C[t]

    if cf is None:
        print(len(ct))
        continue

    if ct is None:
        C[t] = cf
        C[f] = empty
        print(len(cf))
        continue

    if len(cf) <= len(ct):
        for c in cf:
            ct.add(c)
        C[f] = empty
        print(len(ct))
    else:
        for c in ct:
            cf.add(c)
        C[t] = cf
        C[f] = empty
        print(len(cf))
