from bisect import bisect_left

A, B, Q = list(map(int, input().split()))
S = [-10**11] + [int(input()) for _ in range(A)] + [10**11]
T = [-10**11] + [int(input()) for _ in range(B)] + [10**11]

for q in range(Q):
    x = int(input())
    i = bisect_left(S, x)
    j = bisect_left(T, x)

    sl, sr = x-S[i-1], S[i]-x
    tl, tr = x-T[j-1], T[j]-x

    print(min(max(sl, tl),
              max(sr, tr),
              sl*2 + tr,
              tl*2 + sr,
              sr*2 + tl,
              tr*2 + sl))
    
    
