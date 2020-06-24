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
            if k&1: retval = retval * x % self.mod
            k>>=1
            x = x*x % self.mod
        return retval % self.mod

    def modcomb(self, n, k):
        return self.f[n] * self.modpow(self.f[n-k], -1) * self.modpow(self.f[k], -1) % self.mod

N = int(input())
X = list(map(int, input().split()))
D = [X[i+1]-X[i] for i in range(N-1)]

mw = ModWorld(mod=10**9+7)
mw.prepare_factorial(N=10**5)

ans = k = 0
for i, d in enumerate(D):
    k = (k + mw.f[N-1]*mw.modpow(i+1, -1)) % mw.mod
    ans = (ans + d*k) % mw.mod

print(ans)
