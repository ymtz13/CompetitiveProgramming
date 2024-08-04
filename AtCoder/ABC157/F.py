from math import sqrt


def pq(ri, rj, dist):
    # dist = pi + pj
    # ri^2 = pi^2 + q^2 -> pi = sqrt(ri^2-q^2)
    # rj^2 = pj^2 + q^2 -> pj = sqrt(rj^2-q^2)

    ok = 0
    ng = min(ri, rj)
    while ng - ok > 1e-8:
        q = (ng + ok) / 2

        pi = sqrt(ri * ri - q * q)
        pj = sqrt(rj * rj - q * q)
        if dist < pi + pj:
            ok = q
        else:
            ng = q

    q = ok
    p = sqrt(rj * rj - q * q)
    return p, q


# p, q = pq(3, 5, 7)
# print(p, q)
# print(p * p + q * q)
# print((7 - p) * (7 - p) + q * q)


N, K = map(int, input().split())
XYC = [list(map(int, input().split())) for _ in range(N)]


def f(t):
    XYR = [(x, y, t / c) for x, y, c in XYC]

    def g(xs, ys):
        cnt = 0
        for xk, yk, rk in XYR:
            dx = xs - xk
            dy = ys - yk
            if dx * dx + dy * dy < rk * rk + 1e-8:
                cnt += 1
        return cnt >= K

    # F = True
    for i, (xi, yi, ri) in enumerate(XYR):
        if g(xi, yi):
            return True

        for j, (xj, yj, rj) in enumerate(XYR[i + 1 :], i + 1):
            dx = xi - xj
            dy = yi - yj
            distsq = dx * dx + dy * dy
            dist = sqrt(distsq)

            # if dist > ri + rj:
            #     return False

            # if dist + min(ri, rj) < max(ri, rj):
            #     continue

            # F = False

            ex = dx / dist
            ey = dy / dist

            p, q = pq(ri, rj, dist)
            sx = xj + ex * p
            sy = yj + ey * p

            s1x = sx + ey * q
            s1y = sy - ex * q
            s2x = sx - ey * q
            s2y = sy + ex * q

            if g(s1x, s1y) or g(s2x, s2y):
                return True
            # print(i, j, (s1x, s1y), (s2x, s2y))

    return False


ok = 4000 * 100
ng = 0
while ok - ng > 1e-8:
    t = (ok + ng) / 2
    # print(t, f(t))
    if f(t):
        ok = t
    else:
        ng = t

print(ok)
