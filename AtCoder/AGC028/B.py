class Mod:
    def __init__(self, mod, fMax):
        factorial = [1]
        for n in range(1, fMax + 10):
            factorial.append(factorial[-1] * n % mod)

        factorial_inv = [pow(factorial[-1], mod - 2, mod)]
        for n in range(len(factorial) - 1, 0, -1):
            factorial_inv.append(factorial_inv[-1] * n % mod)
        factorial_inv.reverse()

        self.mod = mod
        self.fMax = fMax
        self.factorial = factorial
        self.factorial_inv = factorial_inv

    def comb(self, n, k):
        return (
            self.factorial[n]
            * self.factorial_inv[n - k]
            * self.factorial_inv[k]
            % self.mod
        )


mod = 10**9 + 7

N = int(input())
A = list(map(int, input().split()))

m = Mod(mod, N + 10)

s = 0
for a in A:
    s += a
    s %= mod

Sl = [0]
Sr = [0]
for a in A:
    Sl.append(Sl[-1] + a)
for a in A[::-1]:
    Sr.append(Sr[-1] + a)

T = [None] * (N + 1)
r = 0
for i in range(1, N + 1):
    if T[i] is not None:
        break

    r += Sl[i - 1] + Sr[i - 1]
    r %= mod

    t = (s * i % mod) - r
    t %= mod
    T[i] = T[-i] = t

print(T)

ans = m.factorial[N] * T[N] % mod

ans += m.factorial[N - 1] * T[N - 1] % mod
ans %= mod

for n in range(N-2, 0, -1):
    k = N - n
    kP2 = 
