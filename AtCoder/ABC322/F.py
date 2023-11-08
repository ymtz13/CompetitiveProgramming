class SegTree:
    def __init__(self, N, function, identity, initialData=None):
        L = 1
        M = 1
        while M < N:
            L += 1
            M <<= 1

        segsize = [1 << l for l in range(L)]
        data = [None] * L

        if initialData:
            layer = data[0] = initialData[:M] + [identity] * (M - len(initialData))
            for i in range(1, L):
                layer = data[i] = [function(*v) for v in zip(layer[0::2], layer[1::2])]

        else:
            for l in range(L):
                data[l] = [identity] * (M // segsize[l])

        self.L = L
        self.segsize = segsize
        self.data = data
        self.function = function
        self.bottom = self.data[0]

        self.zip = [(l, segsize[l], data[l]) for l in range(L)]

    def update(self, i, value):
        function = self.function
        layer = self.bottom
        layer[i] = value

        for layer_above in self.data[1:]:
            i >>= 1
            j = i << 1
            layer_above[i] = function(layer[j], layer[j + 1])
            layer = layer_above

    def query(self, qbgn, qend):
        vals = []
        # segs = []

        q = qbgn
        for l, ssize, data in self.zip:
            if q & ssize and q + ssize <= qend:
                # segs.append((q, ssize))
                vals.append(data[q >> l])
                q += ssize

        for l, ssize, data in reversed(self.zip):
            if q + ssize <= qend:
                # segs.append((q, ssize))
                vals.append(data[q >> l])
                q += ssize

        retval = vals[0]
        for val in vals[1:]:
            retval = self.function(retval, val)

        # return segs
        return retval

    def __str__(self):
        s = []
        for l, row in enumerate(self.data[::-1]):
            s.append("{:2d} {}".format(l, row))
        return "\n".join(s)


N, Q = map(int, input().split())
S = input()

identity = (0, 1, 0, 1, 1)
flip = (1, 0, 1, 0, 1)
initial = [identity]
prev = "0"
for i, c in enumerate(S, 1):
    if c != prev:
        initial.append(flip)
    else:
        initial.append(identity)
    prev = c


Queries = [tuple(map(int, input().split())) for _ in range(Q)]


def merge(lv, rv):
    flipL, stk0L, stk1L, leadL, tailL = lv
    flipR, stk0R, stk1R, leadR, tailR = rv

    flip = flipL + flipR
    lead = leadL if flipL else leadL + leadR
    tail = tailR if flipR else tailL + tailR

    if flipL % 2 == 0:
        return (flip, max(stk0L, stk0R, tailL + leadR), max(stk1L, stk1R), lead, tail)
    else:
        return (flip, max(stk0L, stk1R), max(stk1L, stk0R, tailL + leadR), lead, tail)


st = SegTree(N + 2, merge, identity, initial)

ans = []

for c, L, R in Queries:
    if c == 1:
        vL = flip if st.bottom[L] == identity else identity
        vR = flip if st.bottom[R + 1] == identity else identity
        st.update(L, vL)
        st.update(R + 1, vR)

    else:
        res = st.query(L, R + 1)
        cnt = st.query(0, L)

        if cnt[0] % 2 == 0:
            a = res[2]
        else:
            a = res[1]

        ans.append(a)


for a in ans:
    print(a)
