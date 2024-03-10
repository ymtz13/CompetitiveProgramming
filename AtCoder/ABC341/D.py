from math import gcd

N, M, K = map(int, input().split())

G = gcd(N, M)
L = N * M // G

ok = 1 << 70
ng = 0
while ok - ng > 1:
    tgt = (ok + ng) // 2

    xN = tgt // N
    xM = tgt // M
    xL = tgt // L

    if (xN + xM - xL * 2) >= K:
        ok = tgt
    else:
        ng = tgt

print(ok)
