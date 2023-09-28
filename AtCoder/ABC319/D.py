N, M = map(int, input().split())
L = list(map(int, input().split()))

Lmax = max(L)


def line(W):
    if W < Lmax:
        return 1 << 60

    m = 1
    x = 0
    for l in L:
        if x > 0:
            x += 1
        x += l

        if x > W:
            x = l
            m += 1

    return m


ok = sum(L) + N + 10
ng = Lmax - 1

while ok - ng > 1:
    tgt = (ok + ng) // 2

    if line(tgt) <= M:
        ok = tgt
    else:
        ng = tgt

print(ok)
