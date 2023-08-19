N, M = map(int, input().split())
P = []
F = []
for _ in range(N):
    X = list(map(int, input().split()))
    p, _, *f = X
    P.append(p)
    F.append(set(f))

for pi, fi in zip(P, F):
    for pj, fj in zip(P, F):
        if pj > pi:
            continue
        dij = fi.difference(fj)
        if dij:
            continue

        dji = fj.difference(fi)
        if dji or pi - pj > 0:
            print("Yes")
            exit()


print("No")
