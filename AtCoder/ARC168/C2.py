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

    def binom(self, n, k):
        return (
            self.factorial[n]
            * self.factorial_inv[n - k]
            * self.factorial_inv[k]
            % self.mod
        )


mod = 998244353

N, K = map(int, input().split())
S = input()

m = Mod(mod, N + 10)

nA = S.count("A")
nB = S.count("B")
nC = S.count("C")

ans = 0

for sAB in range(K + 1):
    if sAB > nA or sAB > nB:
        continue

    p0 = m.binom(nA, sAB) * m.binom(nB, sAB) % mod
    # print(sAB, p0, m.binom(nA, sAB), m.binom(nB, sAB), "<-sAB")

    nA2 = nA - sAB
    nB2 = nB - sAB

    for sBC in range(K - sAB + 1):
        if sBC > nB2 or sBC > nC:
            continue

        p1 = p0 * m.binom(nB2, sBC) * m.binom(nC, sBC) % mod
        # print(sAB, sBC, p1, m.binom(nB2, sBC), m.binom(nC, sBC), "<-")

        nB3 = nB2 - sBC
        nC3 = nC - sBC

        for sCA in range(K - sAB - sBC + 1):
            if sCA > nC3 or sCA > nA2:
                continue

            p2 = p1 * m.binom(nC3, sCA) * m.binom(nA2, sCA) % mod

            nC4 = nC3 - sCA
            nA4 = nA2 - sCA

            R = (K - sAB - sBC - sCA) // 2
            for rABC in range(R + 1):
                if rABC > nA4 or rABC > nB3 or rABC > nC4:
                    continue

                p3 = p2
                p3 = p3 * m.binom(nA4, rABC) % mod
                p3 = p3 * m.binom(nB3, rABC) % mod
                p3 = p3 * m.binom(nC4, rABC) % mod

                nA5 = nA4 - rABC
                nB5 = nB3 - rABC
                nC5 = nC4 - rABC

                for rCBA in range(R - rABC + 1):
                    if rCBA > nA5 or rCBA > nB5 or rCBA > nC5:
                        continue

                    p4 = p3
                    p4 = p4 * m.binom(nA5, rCBA) % mod
                    p4 = p4 * m.binom(nB5, rCBA) % mod
                    p4 = p4 * m.binom(nC5, rCBA) % mod

                    ans += p4
                    ans %= mod

                    print(sAB, sBC, sCA, rABC, rCBA, p4)


print(ans)
