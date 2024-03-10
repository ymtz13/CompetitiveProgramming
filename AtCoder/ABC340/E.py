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
A = list(map(int, input().split()))
B = list(map(int, input().split()))

p = 0
D = []
for a in A:
    D.append(a - p)
    p = a
D.append(-A[-1])

st = SegTree(N + 1, 0, lambda x, y: x + y, D)


def getAns():
    E = [st.bottom(i) for i in range(N)]
    s = 0
    ans = []
    for e in E:
        s += e
        ans.append(s)
    return ans


for b in B:
    k = st.query(0, b + 1)

    st.update(b, st.bottom(b) - k)
    st.update(b + 1, st.bottom(b + 1) + k)

    nr = N - 1 - b
    kr = min(nr, k)

    if kr:
        # print(f"nr:{nr} kr:{kr}")
        st.update(b + 1, st.bottom(b + 1) + 1)
        st.update(b + kr + 1, st.bottom(b + kr + 1) - 1)

    kk = k - kr
    if not kk:
        # print([b, k], *getAns())
        continue

    kc = kk // N
    kl = kk % N

    st.update(0, st.bottom(0) + kc + (1 if kl else 0))
    if kl:
        st.update(kl, st.bottom(kl) - 1)

    # print([b, k], *getAns())


ans = getAns()
print(*ans)
