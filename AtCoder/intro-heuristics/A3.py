import numpy as np
from itertools import product

D = int(input())
C = np.array(list(map(int, input().split())))
S = np.array([list(map(int, input().split())) for d in range(D)])

L = np.empty(26, int)
L[:] = -1

P2 = list(product(range(26), repeat=2))
P3 = list(product(range(26), repeat=3))

for d in range(0, 363, 3):
    scores = []
    for t in P3:
        LL = L.copy()

        score = 0
        for tt, dd in zip(t, range(d, d+3)):
            LL[tt] = dd
            score += S[d, tt] - np.dot(C, dd-LL)

        scores.append(score)

    smax = scores[0]
    tmax = 0
    for t, s in enumerate(scores):
        if s>smax:
            smax = s
            tmax = t

    for tt, dd in zip(P3[tmax], range(d, d+3)):
        L[tt] = dd
        print(tt+1)

d = 363
scores = []
for t in P2:
    LL = L.copy()

    score = 0
    for tt, dd in zip(t, range(d, d+2)):
        LL[tt] = dd
        score += S[d, tt] - np.dot(C, dd-LL)

    scores.append(score)

smax = scores[0]
tmax = 0
for t, s in enumerate(scores):
    if s>smax:
        smax = s
        tmax = t

for tt, dd in zip(P2[tmax], range(d, d+3)):
    L[tt] = dd
    print(tt+1)
