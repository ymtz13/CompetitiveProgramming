import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# K-a <= x <= K-1

from time import time

t = time()

dp_L = [[False]*K for _ in range(N)]
dp_L[0][0] = True
for i, a in enumerate(A[:-1]):
    dp_L_next = dp_L[i+1]
    for j, d in enumerate(dp_L[i]):
        dp_L_next[j] = d
    if a>=K: continue
    for j, d in enumerate(dp_L[i][:-a]):
        dp_L_next[j+a] |= d

dp_R = [[False]*K for _ in range(N)]
dp_R[0][0] = True
for i, a in enumerate(A[:0:-1]):
    dp_R_next = dp_R[i+1]
    for j, d in enumerate(dp_R[i]):
        dp_R_next[j] = d
    if a>=K: continue
    for j, d in enumerate(dp_R[i][:-a]):
        dp_R_next[j+a] |= d


print(time()-t)
# for i, d in enumerate(dp_L):
#     print(i,d)
# 
# for i, d in enumerate(dp_R):
#     print(i, d)

t = time()

ans = 0
for i, a in enumerate(A):
    dl = dp_L[i]
    dr = dp_R[-(i+1)]
    
    noneed = True
    ml = -K
    for j in range(K):
        fl = dl[j]
        fr = dr[K-1-j]
        if fl: ml = j
        if fr and j-ml<a:
            noneed = False
            break
    if noneed: ans+=1

print(ans)

print(time()-t)
