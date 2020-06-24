from bisect import bisect_left

N, Q = [int(c) for c in input().split()]

M = [10**10]*Q

STX = []
for n in range(N):
    s,t,x = [int(c) for c in input().split()]
    STX.append((s,t,x))

D = [int(input()) for q in range(Q)]

for s,t,x in STX:
    d_l = bisect_left(D, s-x)
    d_r = bisect_left(D[d_l:], t-x)+d_l
    for d in range(d_l, d_r):
        M[d] = min(x,M[d])

for q in range(Q):
    m = -1 if M[q] == 10**10 else M[q]
    print(m)
