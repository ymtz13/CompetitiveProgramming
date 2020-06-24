N, K = [int(c) for c in input().split()]
nB, nR = K, N-K

if nR==0:
    print(1)
    for k in range(2, K+1):
        print(0)
    exit()

mod = int(1e9+7)

binom = [[0 for _ in range(2001)] for _ in range(2001)]
binom[0][0] = 1
for n in range(1, 2001):
    binom[n][0] = 1
    for k in range(1,2001):
        binom[n][k] = (binom[n-1][k] + binom[n-1][k-1]) % mod
        
for k in range(1, K+1):
    blue   = binom[nB-1][k-1]
    red_m1 = binom[nR-1][k-2] if k>=2 else 0
    red_0  = binom[nR-1][k-1]
    red_p1 = binom[nR-1][k  ]

    print((blue*(red_m1 + red_0*2 + red_p1)) % mod )
