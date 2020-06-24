class ModWorld:
    def __init__(self, mod):
        self.mod = mod

    def prepare_factorial(self, N):
        self.f = [1] # f[n] := n!
        p = 1
        for i in range(1,N+1):
            p = (p*i) % self.mod
            self.f.append(p)

    def modpow(self, x, k):
        x %= self.mod
        k %= self.mod-1 # a^(p-1) = 1
        retval = 1
        while k:
            if k&1: retval = retval*x%self.mod
            k>>=1
            x = x*x % self.mod
        return retval % self.mod

    def modcomb(self, n, k):
        return self.f[n] * self.modpow(self.f[n-k], -1) * self.modpow(self.f[k], -1) % self.mod

mw = ModWorld(mod=10**9+7)
mw.prepare_factorial(N=10**5)

import numpy as np

N = int(input())
X = np.array(list(map(int, input().split())))[::-1]

ans = (X[0]-X[1]) * mw.f[N-1]

M = np.eye(N-1, dtype=int)

print('ans', ans)

for i in range(N-2):
    for r in range(i+1):
        M[r]*=i+1-r
    M[1:i+1, i+1] = M[0,0] - np.sum(M[1:i+1, :i+1], axis=1)
    M[i+1,i+1] = M[0,0]
    M%=mw.mod
    kk = np.sum(M, axis=0)[:i+2]
    tt = kk * (X[:i+2]-X[i+2])
    print(i, mw.f[N-i-2],  kk, tt, sum(kk))
    xx = mw.modpow(sum(kk), -1)
    ans += np.sum(tt) * mw.f[N-1] * xx
    ans %= mw.mod
    print(ans, M)
    

print(ans)
