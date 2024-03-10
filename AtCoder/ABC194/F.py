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
mmod = Mod(mod, 1000000)

N, K = input().split()


N = int(N, 16) + 1
A = []
while N:
    A.append(N % 16)
    N //= 16

A.reverse()
print(A)

K = int(K)

S = set()
ans = 0
for nl, a in enumerate(A):
    nr = len(A) - 1 - nl

    n0 = n1 = 0
    for b in range(a):
        if b in S or (b == 0 and nl == 0):
            n0 += 1
        else:
            n1 += 1
    R = 16 - len(S)

    v0 = v1 = 0
    for d, k in enumerate(range(K, 0, -1)):
        sign = -1 if d & 1 else 1

        r0 = k - len(S)
        r1 = r0 - 1

        if r0 >= 0:
            v0 += sign * mmod.comb(R, r0) * pow(k, nr, mod) % mod
            v0 %= mod

        if r1 >= 0:
            v1 += sign * mmod.comb(R, r1) * pow(k, nr, mod) % mod
            v1 %= mod

    print(nl, (n0, n1), (v0, v1))

    ans += n0 * v0 % mod
    ans += n1 * v1 % mod
    ans %= mod

    S.add(a)

if K == 1:
    ans -= 1
    ans %= mod

print(ans)
