def z_algo(S: str):
    L = len(S)
    ret = [L]
    i = 1
    jnxt = 0
    while i < L:
        j = jnxt
        while i + j < L and S[j] == S[i + j]:
            j += 1

        ret.append(j)

        jnxt = 0
        for k in range(1, j):
            if k + ret[k] >= j:
                jnxt = j - k
                break
            ret.append(ret[k])

        i = len(ret)

    return ret


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


S = input()
T = input()
N = len(T)

Z = z_algo(f"{S}_{T}")[-N:]

st = SegTree(N + 10, 1 << 60, min)
st.update(0, 0)

for i, z in enumerate(reversed(Z), 1):
    if z == 0:
        continue
    v = st.query(max(0, i - z), i)
    st.update(i, v + 1)

ans = st.query(N, N + 1)
print(ans if ans < N + 5 else -1)
