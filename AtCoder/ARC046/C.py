from collections import deque


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
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(M)]

S = list(set([b for _, b in AB] + [c for c, _ in CD]))
S.sort()
T = {v: i for i, v in enumerate(S)}

st = SegTree(len(T) + 10, -1, max)

AB.sort(reverse=True)

DC = [(d, c) for c, d in CD]
DC.sort(reverse=True)

AB = deque(AB)
DC = deque(DC)

cnt = [0] * len(S)
ans = 0

while DC:
    d, c = DC.popleft()

    while AB and AB[0][0] >= d:
        _, b = AB.popleft()

        t = T[b]
        st.update(t, t)
        cnt[t] += 1

    tc = T[c]
    m = st.query(0, tc + 1)

    if m >= 0:
        cnt[m] -= 1
        if cnt[m] == 0:
            st.update(m, -1)
        ans += 1

print(ans)
