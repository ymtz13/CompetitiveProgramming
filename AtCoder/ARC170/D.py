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


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    b = B[0]
    for i, a in enumerate(A):
        if a < b:
            continue
        if (i == 0 or A[i - 1] <= a - b) and (i == N - 1 or A[i + 1] >= a + b):
            return "Bob"

    C = [(a * 2 + 0) * N + i for i, a in enumerate(A)] + [
        (b * 2 + 1) * N + i for i, b in enumerate(B)
    ]
    C.sort()

    nextB = [None] * N

    DL = []
    d1 = d2 = 1 << 60
    Z = []
    for c in C:
        ct, i = c // N, c % N
        c, t = ct // 2, ct % 2
        if t == 0:
            d2 = d1
            d1 = c
            Z.append(i)
        else:
            DL.append([c - d1, c - d2])
            for z in Z:
                nextB[z] = i
            Z = []

    D = [a * 2 + 1 for a in A] + [b * 2 + 0 for b in B]
    D.sort(reverse=True)

    DR = []
    d1 = d2 = 1 << 60
    for c in C:
        c, t = c // 2, c % 2
        if t == 1:
            d2 = d1
            d1 = c
        else:
            DR.append([d1 - c, d2 - c])
    DR.reverse()

    DD = [sorted(dl + dr) for dl, dr in zip(DL, DR)]
    D1 = [dd[0] for dd in DD]
    D2 = [dd[1] for dd in DD]


T = int(input())

for _ in range(T):
    print(solve())
