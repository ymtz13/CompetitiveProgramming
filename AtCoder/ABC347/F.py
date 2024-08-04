class SegTree:
    def __init__(self, N, identity, function, initial=[]):
        # L = 3, M = 4
        # l=2 : 1
        # l=1 : 10      11
        # l=0 : 100 101 110 111

        L = 1
        M = 1  # N以上の最小の2冪
        while M < N:
            L += 1
            M <<= 1

        segsize = [1 << l for l in range(L)]

        data = [identity] * M + initial[:M] + [identity] * (M - len(initial))
        if initial:
            for i in range(M - 1, 0, -1):
                j = i << 1
                data[i] = function(data[j], data[j + 1])

        self.L = L
        self.M = M
        self.segsize = segsize
        self.data = data
        self.function = function

        self.zip = [(l, segsize[l]) for l in range(L)]

    def update(self, i, value):
        data = self.data
        function = self.function

        i += self.M
        data[i] = value
        while i > 1:
            i >>= 1
            j = i << 1
            data[i] = function(data[j], data[j + 1])

    def segments(self, qbgn, qend):
        M = self.M

        segs = []

        q = qbgn
        for l, ssize in self.zip:
            if q & ssize and q + ssize <= qend:
                segs.append((q + M) >> l)
                q += ssize

        for l, ssize in reversed(self.zip):
            if q + ssize <= qend:
                segs.append((q + M) >> l)
                q += ssize

        return segs

    def query(self, qbgn, qend):
        function = self.function
        data = self.data

        segs = self.segments(qbgn, qend)

        retval = data[segs[0]]
        for i in segs[1:]:
            retval = function(retval, data[i])

        return retval

    def bottom(self, i):
        return self.data[self.M + i]

    def __str__(self):
        s = []
        for l in range(self.L):
            s.append("{:2d} {}".format(l, self.data[1 << l : 2 << l]))
        return "\n".join(s)


N, M = map(int, input().split())
A = [[0] * (N + 1)]
A.extend([[0] + list(map(int, input().split())) for _ in range(N)])

for i in range(N):
    for j in range(1, N + 1):
        A[i + 1][j] += A[i][j]

for i in range(N):
    for j in range(1, N + 1):
        A[j][i + 1] += A[j][i]

K = N - M + 1
B = [[0] * (N - M + 1) for _ in range(N - M + 1)]
for i in range(N - M + 1):
    for j in range(N - M + 1):
        B[i][j] = A[i + M][j + M] - A[i + M][j] - A[i][j + M] + A[i][j]

RowMax = [max(row) for row in B]
RowMaxSt = SegTree(K, 0, max, RowMax)

MaxColL = []
MaxColR = []
maxColL = [0] * K
maxColR = [0] * K
for icol in range(K):
    maxColL = [max(prev, row[icol]) for prev, row in zip(maxColL, B)]
    MaxColL.append(maxColL)
    maxColR = [max(prev, row[-1 - icol]) for prev, row in zip(maxColR, B)]
    MaxColR.append(maxColR)

ans = 0
for icol in range(K):
    ncolL = max(0, icol - M - 1)
    ncolR = max(0, K - icol - 1 - M - 1)

    stColL = SegTree(K, 0, max, MaxColL[ncolL - 1]) if ncolL else None
    stColR = SegTree(K, 0, max, MaxColR[ncolR - 1]) if ncolR else None

    for irow in range(K):
        nrow1 = max(0, irow - M - 1)
        nrow2 = max(0, K - irow - 1 - M - 1)

        vRow1 = RowMaxSt.query(0, nrow1) if nrow1 else 0
        vRow2 = RowMaxSt.query(K - nrow2, K) if nrow2 else 0

        vColL1 = stColL.query(0, irow + 1) if stColL else 0
        vColL2 = stColL.query(irow + 1, K) if irow + 1 < K and stColL else 0
        vColR1 = stColR.query(0, irow) if irow and stColR else 0
        vColR2 = stColR.query(irow, K) if stColR else 0

        v0 = B[irow][icol]
        v1 = max(vRow1, vColL1, vColR1)
        v2 = max(vRow2, vColL2, vColR2)
        ans = max(ans, v0 + v1 + v2)

print(ans)
