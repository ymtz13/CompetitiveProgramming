N, K = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))

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
            if k&1: retval = x * retval % self.mod
            k>>=1
            x = x*x % self.mod
        return retval % self.mod

    def modcomb(self, n, k):
        return self.f[n] * self.modpow(self.f[n-k], -1) * self.modpow(self.f[k], -1) % self.mod

mw = ModWorld(mod=10**9+7)
mw.prepare_factorial(N=10**5)

ans = 0
for i in range(N):
    if N-1-i<K-1: break
    comb = mw.modcomb(N-1-i, K-1)
    ans -= A[i] * comb
    ans += A[-(i+1)] * comb
    ans %= mw.mod
print(ans)
    
