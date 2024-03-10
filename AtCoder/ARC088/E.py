from collections import defaultdict, deque


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


def f(A):
    N = len(A) + 5
    st = SegTree(N, 0, lambda x, y: x + y)
    cnt = 0
    for a in A:
        cnt += st.query(a, N)
        st.update(a, 1)

    return cnt


S = input()

if len(S) == 1:
    print(0)
    exit()

D = defaultdict(int)
for c in S:
    D[c] += 1

odd = [v for v in D.values() if v % 2]
if len(odd) > 1:
    print(-1)
    exit()

Z = defaultdict(int)
X = []
L, C, R = 0, 1, 2
for c in S:
    Z[c] += 1
    z = Z[c]
    d = D[c]

    if d % 2 and z * 2 - 1 == d:
        X.append(C)
    elif z * 2 <= d:
        X.append(L)
    else:
        X.append(R)

# print(X)

T = [(x, i, c) for i, (x, c) in enumerate(zip(X, S))]
T.sort()

# print(T)

p1 = f([i for _, i, _ in T])
# print(p1)

TL = T[: len(X) // 2]
TR = T[-(len(X) // 2) :]

TL = [c for _, _, c in TL]
TR = [c for _, _, c in TR][::-1]

# print(TL)
# print(TR)

K = defaultdict(deque)
for i, c in enumerate(TL):
    K[c].append(i)

V = []
for c in TR:
    V.append(K[c].popleft())

# print(V)

p2 = f(V)

print(p1 + p2)
