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


INF = 1 << 60


def f(P):
    M = len(P) + 10
    ret = [INF]

    st0 = SegTree(M, -INF, max)
    st1 = SegTree(M, -INF, max)

    st0.update(P[0], 0)

    for i, p in enumerate(P[1:], 1):
        pprev = P[i - 1]

        if pprev < p:
            if i % 2 == 0:
                u = st0.query(0, p)
                v = st1.query(p, M)
            else:
                u = st1.query(0, p)
                v = st0.query(p, M)
        else:
            if i % 2 == 0:
                u = st0.query(p, M)
                v = st1.query(0, p)
            else:
                u = st1.query(p, M)
                v = st0.query(0, p)

        r = i - 1 - max(u, v)
        ret.append(r)

        if i % 2 == 0:
            st0.update(p, i)
        else:
            st1.update(p, i)

    return ret


def solve(N, P):
    AL = f(P)
    AR = f(P[::-1])[::-1]

    ans = []

    p = P[0]
    a = -1
    for i, (p1, p2) in enumerate(zip(P[1::2], P[2::2])):
        if p < min(p1, p2) or max(p1, p2) < p:
            a = i * 2 + 3
            break
    ans.append(a)

    for i, (pl, p, pr) in enumerate(zip(P, P[1:], P[2:]), 1):
        if p < min(pl, pr) or max(pl, pr) < p:
            ans.append(3)
            continue

        vL = AL[i]
        vR = AR[i]
        m = min(vL, vR)

        a = (m // 2) * 2 + 1 + 2
        ans.append(a)

    p = P[-1]
    a = -1
    for i, (p1, p2) in enumerate(zip(P[-2::-2], P[-3::-2])):
        if p < min(p1, p2) or max(p1, p2) < p:
            a = i * 2 + 3
            break
    ans.append(a)

    ans = [a if a <= N else -1 for a in ans]
    return ans


from random import shuffle, seed

seed(1)


def naive(N, P):
    ret = [-1] * N
    for k in range(3, N + 1, 2):
        for l in range(N - k + 1):
            pp = P[l : l + k]
            med = sorted(pp)[k // 2]
            for i in range(l, l + k):
                if P[i] != med and ret[i] == -1:
                    ret[i] = k
    return ret


# for _ in range(1 << 20):
#     N = 7
#     P = list(range(1, N + 1))
#     shuffle(P)
#     ans = solve(N, P)
#     nai = naive(N, P)
#     assert ans == nai, (P, ans, nai)


N = int(input())
P = list(map(int, input().split()))
ans = solve(N, P)
print(*ans)
