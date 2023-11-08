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


H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2
M = H2 * W2

T = ["." * W2]
for h in range(H):
    T.append(f".{input()}.")
T.append("." * W2)

uf = UF(M)

cnt = 0
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if T[h][w] != "#":
            continue
        cnt += 1
        for dh in (-1, 0, 1):
            for dw in (-1, 0, 1):
                hh = h + dh
                ww = w + dw

                if T[hh][ww] == "#":
                    uf.union(h * W2 + w, hh * W2 + ww)

ans = cnt + uf.n - M

# print(M, uf.n, cnt)
print(ans)
