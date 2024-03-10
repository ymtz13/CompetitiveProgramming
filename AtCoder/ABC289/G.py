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
B = list(map(int, input().split()))
C = list(map(int, input().split()))

B.sort(reverse=True)
B = [None] + B

stL = SegTree(M + 2, 0, lambda x, y: x if x else y)
stR = SegTree(M + 2, 0, lambda x, y: y if y else x)

M1 = M + 1

stL.update(0, 1)
stR.update(0, 1)
stL.update(M1, N)
stR.update(M1, N)

CI = [c * M1 + i for i, c in enumerate(C, 1)]
CI.sort()

K = 1
T = 0
while K < M + 2:
    K <<= 1
    T += 1

ans = [None] * M1

for k in range(K):
    x = [(k >> i) & 1 for i in range(T)]
    y = sum([xx << i for i, xx in enumerate(reversed(x))])

    # print(f"{k:05b} {y:05b} y:{y} T:{T}")

    if not 1 <= y <= M:
        continue

    ci = CI[y - 1]
    c, i = ci // M1, ci % M1

    nl = stR.query(0, y)
    nr = stL.query(y, M1 + 1)

    # print(f"{k:05b} {y:05b} y:{y}, (vl, vr)=({nl},{nr})")

    n = nl
    s = n * (c + B[n])
    for nn in range(nl + 1, nr + 1):
        ss = nn * (c + B[nn])
        if ss > s:
            s = ss
            n = nn

    ans[i] = s

    stR.update(y, n)
    stL.update(y, n)

print(*ans[1:])
