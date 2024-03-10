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


mod = 998244353

H, W = map(int, input().split())

H2 = H + 2
W2 = W + 2

M = [2] * (H2 * W2)

for h in range(1, H + 1):
    S = input()
    for w, c in enumerate(S, 1):
        d = 0 if c == "." else 1
        M[h * W2 + w] = d

uf = UF(len(M))

for h in range(1, H + 1):
    for w in range(1, W + 1):
        i = h * W2 + w
        c = M[i]

        if c == 0:
            continue

        if c == M[i + 1]:
            uf.union(i, i + 1)
        if c == M[i + W2]:
            uf.union(i, i + W2)

X = [0, 0, 0, 0, 0]

green = set()
for h in range(1, H + 1):
    for w in range(1, W + 1):
        i = h * W2 + w
        c = M[i]

        if c != 0:
            green.add(uf.find(i))
            continue

        s = set()
        if M[i - 1] == 1:
            s.add(uf.find(i - 1))
        if M[i + 1] == 1:
            s.add(uf.find(i + 1))
        if M[i - W2] == 1:
            s.add(uf.find(i - W2))
        if M[i + W2] == 1:
            s.add(uf.find(i + W2))

        X[len(s)] += 1

red = sum(X)
inv = pow(red, mod - 2, mod)

ans = len(green)
for v, x in enumerate(X):
    ans += (1 - v) * x * inv % mod
    ans %= mod

print(ans)
