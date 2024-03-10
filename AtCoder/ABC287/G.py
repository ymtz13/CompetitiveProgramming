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


N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

Queries = [
    (1, 1, 3),
    (1, 1, 3),
    (1, 2, 3),
    (1, 3, 3),
    (1, 4, 3),
    (1, 5, 3),
    # (1, 4, 4),
    # (1, 5, 4),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (3, 11),
    (3, 1000000000),
    # (3, 4),
    # (2, 1, 0),
    # (2, 3, 0),
    # (3, 4),
    # (3, 2),
]
Q = len(Queries)

A = [None] + [a for a, _ in AB]
B = [None] + [b for _, b in AB]

INF = 1 << 62
P = list(set(A[1:] + [q[2] for q in Queries if q[0] == 1] + [-INF]))
P.sort(reverse=True)
D = {v: i for i, v in enumerate(P)}

initC = [0] * len(P)
for a, b in AB:
    initC[D[a]] += b

initS = [0] * len(P)
for i, (c, p) in enumerate(zip(initC, P)):
    initS[i] = c * p

initC[D[-INF]] = INF
initS[D[-INF]] = -INF

stC = SegTree(len(P), 0, lambda x, y: x + y, initC)
stS = SegTree(len(P), 0, lambda x, y: x + y, initS)

# for i, (c, p) in enumerate(zip(initC, P)):
#     stC.update(i, c)
#     stS.update(i, c * p)

# stC.update(D[-INF], INF)
# stS.update(D[-INF], -INF)

ans = []

# print(P)

for query in Queries:
    t = query[0]

    if t == 1:
        _, x, y = query
        pold = A[x]
        iold = D[pold]
        inew = D[y]
        diff = B[x]
        A[x] = y

        if iold == inew:
            continue

        cntold = stC.bottom(iold) - diff
        cntnew = stC.bottom(inew) + diff
        stC.update(iold, cntold)
        stC.update(inew, cntnew)
        stS.update(iold, cntold * pold)
        stS.update(inew, cntnew * y)

    if t == 2:
        _, x, y = query
        p = A[x]
        i = D[p]
        diff = y - B[x]
        B[x] = y

        if diff == 0:
            continue

        cnt = stC.bottom(i) + diff
        stC.update(i, cnt)
        stS.update(i, cnt * p)

    if t == 3:
        _, x = query

        ss = -INF
        ok = len(P)
        ng = 0
        while ok - ng > 1:
            tgt = (ok + ng) // 2
            s = stC.query(0, tgt)
            if x <= s:
                ok = tgt
                ss = s
            else:
                ng = tgt

        if ok == len(P):
            ans.append(-1)
            continue

        r = ss - x
        p = P[ok - 1]
        a = stS.query(0, ok) - r * p
        ans.append(a)

        # print(f"ok:{ok}, ss:{ss}, x:{x}, r:{r}, p:{p}, ans:{a}")
        # print(stC)
        # print(stS)


for a in ans:
    print(max(-1, a))
