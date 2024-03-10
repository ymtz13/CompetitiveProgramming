from collections import deque

H, W = map(int, input().split())
HW = H * W

I = [0, 1, W, W + 1]

T = list(range(1, HW + 1))
Ttup = tuple(T)

S = []
for _ in range(H):
    S.extend(map(int, input().split()))
Stup = tuple(S)


def rot(X, h0, w0):
    Y = X[:]
    hz = h0 + H - 2
    wz = w0 + W - 2

    for h in range(H - 1):
        for w in range(W - 1):
            Y[(h0 + h) * W + w0 + w] = X[(hz - h) * W + wz - w]

    return Y


def p(X):
    for h in range(H):
        print(X[h * W : h * W + W])


def g(X0):
    Xs = [set() for _ in range(11)]
    queue = deque([(0, -1, X0)])

    while queue:
        d, i, X = queue.popleft()
        Xs[d].add(tuple(X))
        if d == 10:
            continue

        if i != 0:
            queue.append((d + 1, 0, rot(X, 0, 0)))
        if i != 1:
            queue.append((d + 1, 1, rot(X, 0, 1)))
        if i != 2:
            queue.append((d + 1, 2, rot(X, 1, 0)))
        if i != 3:
            queue.append((d + 1, 3, rot(X, 1, 1)))

    return Xs


Ts = g(T)
Ss = g(S)

for i, ts in enumerate(Ts):
    if Stup in ts:
        print(i)
        exit()

for i, ts in enumerate(Ts[1:], 11):
    if ts & Ss[10]:
        print(i)
        exit()

print(-1)
