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
