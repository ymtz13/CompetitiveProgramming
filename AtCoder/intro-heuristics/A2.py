import numpy as np

D = int(input())
C = np.array(list(map(int, input().split())))
S = np.array([list(map(int, input().split())) for d in range(D)])

L = np.empty(26, int)
L[:] = -1

score = 0
for d in range(D):
    scores_ = []
    for t in range(26):
        d_bkp = L[t]
        L[t] = d
        scores_.append(score + S[d, t] - np.dot(C, d-L))
        L[t] = d_bkp

    smax = scores_[0]
    tmax = 0
    for t, s in enumerate(scores_):
        if s>smax:
            smax = s
            tmax = t

    L[tmax] = d
    score = smax
    print(tmax+1)
