import numpy as np

D = int(input())
C = np.array(list(map(int, input().split())))
S = np.array([list(map(int, input().split())) for d in range(D)])

L = np.empty(26, int)
L[:] = -1

score = 0
for d in range(D):
    t = int(input())-1
    L[t] = d
    score += S[d, t] - np.dot(C, d-L)
    print(score)
