class SegTree:
    def __init__(self, N, function, identity, initial=[]):
        # L = 3, M = 4
        # l=2 : 1
        # l=1 : 10      11
        # l=0 : 100 101 110 111

        L = 1
        M = 1  # N以上の最小の整数
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


s = SegTree(100, lambda x, y: x + y, 0)
print(s)

s.update(5, 6)
s.update(9, 7)
s.update(3, 3)

print(s)

arr = [0] * 100
arr[5] = 6
arr[9] = 7
arr[3] = 3


def flat(segs):
    retval = []
    for q, ssize in segs:
        retval.extend(list(range(q, q + ssize)))
    return retval


def test(segs, qbgn, qend):
    assert flat(segs) == list(range(qbgn, qend))
    cnt = [0] * 1000
    for _, ssize in segs:
        cnt[ssize] += 1
    assert max(cnt) <= 2


def testval(retval, qbgn, qend):
    assert retval == sum(arr[qbgn:qend])


for qbgn in range(10):
    for qend in range(qbgn + 1, 101):
        # test(s.query(qbgn, qend), qbgn, qend)
        # print(qbgn, qend, s.query(qbgn, qend))
        testval(s.query(qbgn, qend), qbgn, qend)

st = SegTree(10, lambda x, y: x + y, 0, list(range(20)))
print(st)
