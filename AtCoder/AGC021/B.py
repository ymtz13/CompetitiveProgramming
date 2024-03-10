from math import atan2, tau, pi

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

if N == 2:
    print(0.5)
    print(0.5)
    exit()

for i, (xi, yi) in enumerate(P):
    T = []
    for j, (xj, yj) in enumerate(P):
        if i == j:
            continue

        x = xi - xj
        y = yi - yj

        t = atan2(y, x)

        T.append(t)
        T.append(t + tau)

    T.sort()
    m = max([t2 - t1 for t1, t2 in zip(T, T[1:])])

    v = max(0, -pi + m)

    print(v / tau)
