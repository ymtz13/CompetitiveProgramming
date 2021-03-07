N, K = map(int, input().split())
P = [None] + list(map(int, input().split()))
C = [None] + list(map(int, input().split()))

R = [False] * (N+1)
S = []

for st in range(1, N+1):
    if R[st]: continue
    loop = []
    x = st
    while not R[x]:
        loop.append(C[x])
        R[x] = True
        x = P[x]

    if max(loop)<=0:
        S.append(max(loop))
        continue

    L = len(loop)
    K0 = K//L
    K1 = K%L

    T = [0]
    for c in loop: T.append(T[-1]+c)
    tot = T[-1]

    smax = smax_l = 0
    for i in range(L):
        for j in range(i, L):
            l = j-i+1
            
            ss = T[j+1]-T[i]
            smax = max(smax, ss)
            smax = max(smax, tot-ss)
            if l  <=K1: smax_l = max(smax_l, ss)
            if L-l<=K1: smax_l = max(smax_l, tot-ss)

    s = smax_l + K0*max(0,tot)
    if K0>0: s = max(s, smax+(K0-1)*max(0,tot))
    S.append(s)

print(max(S))
