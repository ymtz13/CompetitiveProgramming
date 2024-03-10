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


oa = ord("a")

mod = 10**9 + 7
M = 29

N, Q = map(int, input().split())
S = [ord(c) - oa + 1 for c in input()]
Queries = [tuple(input().split()) for _ in range(Q)]

Sinv = S[::-1]

F = [1]
for _ in range(N - 1):
    F.append(F[-1] * M % mod)

TL = [c * f % mod for c, f in zip(S, F)]
TR = [c * f % mod for c, f in zip(Sinv, F)]

stL = SegTree(N, 0, lambda x, y: x + y, TL)
stR = SegTree(N, 0, lambda x, y: x + y, TR)

for t, v1, v2 in Queries:
    if t == "1":
        xL = int(v1) - 1
        xR = N - 1 - xL
        c = ord(v2) - oa + 1
        stL.update(xL, c * F[xL] % mod)
        stR.update(xR, c * F[xR] % mod)
        S[xL] = c

    else:
        L1 = int(v1) - 1
        R1 = int(v2)

        L2 = N - R1
        R2 = N - L1

        z1 = stL.query(L1, R1)
        z2 = stR.query(L2, R2)

        t1 = z1 * pow(F[L1], mod - 2, mod) % mod
        t2 = z2 * pow(F[L2], mod - 2, mod) % mod

        if t1 == t2:
            print("Yes")
            # ss = S[L1:R1]
            # print("Yes" if ss == ss[::-1] else "No")
        else:
            print("No")
