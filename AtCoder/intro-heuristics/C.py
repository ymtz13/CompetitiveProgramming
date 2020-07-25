import numpy as np
from bisect import bisect_left

D = int(input())
C = np.array(list(map(int, input().split())))
S = np.array([list(map(int, input().split())) for d in range(D)])

L = np.empty(26, int)
L[:] = -1

X = [[-1] for _ in range(26)]
T = []

score = 0
for d in range(D):
    t = int(input())-1
    T.append(t)
    L[t] = d
    score += S[d, t] - np.dot(C, d-L)
    X[t].append(d)

for x in X:
    x.append(D)
    
M = int(input())
for _ in range(M):
    d, q = map(int, input().split())
    d-=1
    q-=1

    t = T[d]
    T[d] = q
    
    i = bisect_left(X[t], d)
    d_prev = X[t][i-1]
    d_next = X[t][i+1]
    
    dd = d-d_prev-1
    score += C[t]*(dd+1)*dd//2
    dd = d_next-d-1
    score += C[t]*(dd+1)*dd//2
    dd = d_next-d_prev-1
    score -= C[t]*(dd+1)*dd//2

    X[t].pop(i)
    
    i = bisect_left(X[q], d)
    d_prev = X[q][i-1]
    d_next = X[q][i]
    
    dd = d-d_prev-1
    score -= C[q]*(dd+1)*dd//2
    dd = d_next-d-1
    score -= C[q]*(dd+1)*dd//2
    dd = d_next-d_prev-1
    score += C[q]*(dd+1)*dd//2

    X[q].insert(i, d)

    score += S[d,q] - S[d,t]

    print(score)
