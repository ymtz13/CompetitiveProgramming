from collections import defaultdict

INF = 1 << 60

N, H = map(int, input().split())

TD = defaultdict(int)
for _ in range(N):
    t, d = map(int, input().split())
    TD[d] = max(TD[d], t)

TD = list(TD.items())
TD.sort(reverse=True)


X = [TD[0]]
for dt in TD[1:]:
    if dt[1] > X[-1][1]:
        X.append(dt)

X.append((1e-60, INF))


dt = X[0]
prevT = dt[1]
prevD = dt[0]
R = [(prevT, prevT, prevD)]

for i, (d, t) in enumerate(X[1:], 1):
    turn = (prevT * prevD + d - 1) // d
    if turn <= t:
        if turn - 1 > prevT:
            R.append((turn - 1, prevT, prevD))
        R.append((t, t, d))
        prevT = t
        prevD = d
    else:
        R.append((t, prevT, prevD))


def dd(turn, t):
    t1 = min(t, turn)
    t2 = max(0, turn - t)
    return t1 * (t1 + 1) // 2 + t * t2


def damage(turn):
    retval = 0
    prevT = 0
    for t, xt, xd in R:
        t0 = prevT
        t1 = min(t, turn)
        retval += xd * (dd(t1, xt) - dd(t0, xt))

        prevT = t
        if t >= turn:
            break

    return retval


# for turn in range(1, 20):
#     print(turn, damage(turn))

ng = 0
ok = H
while ok - ng > 1:
    tgt = (ok + ng) // 2
    if damage(tgt) >= H:
        ok = tgt
    else:
        ng = tgt

print(ok)
