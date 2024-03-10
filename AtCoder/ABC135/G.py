def z_algo(S: str):
    L = len(S)
    ret = [L]
    i = 1
    jnxt = 0
    while i < L:
        j = jnxt
        while i + j < L and S[j] == S[i + j]:
            j += 1

        ret.append(j)

        jnxt = 0
        for k in range(1, j):
            if k + ret[k] >= j:
                jnxt = j - k
                break
            ret.append(ret[k])

        i = len(ret)

    return ret


class UF:
    def __init__(self, N):
        self.uf = [-1] * N
        self.n = N

    def find(self, x):
        if self.uf[x] < 0:
            return x
        self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def size(self, x):
        return -self.uf[self.find(x)]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size(x) > self.size(y):
            x, y = y, x
        self.uf[y] += self.uf[x]
        self.uf[x] = y
        self.n -= 1


def solve(S, T):
    s = len(S)
    t = len(T)

    S = S * (t * 2 // s + 2)

    Z = z_algo(f"{T}_{S}")[t + 1 :]

    Z = [z // t for z in Z]

    uf = UF(s)

    for i, z in enumerate(Z[:s]):
        if z:
            j = (i + t) % s

            if uf.find(i) == uf.find(j):
                print(-1)
                exit()

            uf.union(i, j)

    ans = max([uf.size(i) for i in range(s)]) - 1
    return ans


S = input()
T = input()

ans = solve(S, T)
print(ans)
