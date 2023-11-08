from collections import deque
from time import perf_counter


class LazySegTree:
    def __init__(self, N, identity, function, mapping, composition, initial=[]):
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

        self.lazy = [None] * len(data)
        self.mapping = mapping
        self.composition = composition

        self.seglength = [0]
        self.lbound = [0]
        self.rbound = [0]
        for ssize in reversed(self.segsize):
            self.seglength.extend([ssize] * (M // ssize))
            self.lbound.extend(list(range(0, M, ssize)))
            self.rbound.extend(list(range(ssize, M + 1, ssize)))

        # performance measurement
        self.t_segments = self.c_segments = 0
        self.t_set_lazy = self.c_set_lazy = 0
        self.t_resolve = self.c_resolve = 0
        self.t_ancestors = self.c_ancestors = 0
        self.t_update = self.c_update = 0
        self.t_query = self.c_query = 0

    def segments2(self, qbgn, qend):
        lbound = self.lbound
        # seglength = self.seglength
        rbound = self.rbound

        segments = deque()
        ancestors = []  # segmentsの祖先ノード（上のレイヤーから）
        others = []  # ancestorsの子ノードでancestorsでもsegmentsでもないノード

        queue = deque([1])
        left_edge = self.M
        while queue:
            i = queue.popleft()
            l = lbound[i]
            # r = l + seglength[i]
            r = rbound[i]

            if r <= qbgn or qend <= l:
                others.append(i)
                continue

            if qbgn <= l and r <= qend:
                if l < left_edge:
                    segments.appendleft(i)
                    left_edge = l
                else:
                    segments.append(i)
                continue

            ancestors.append(i)
            j = i << 1
            queue.append(j)
            queue.append(j + 1)

        return list(segments), ancestors, others

    def segments(self, qbgn, qend):
        # bgn = perf_counter()

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

        # self.t_segments += perf_counter() - bgn
        # self.c_segments += 1

        return segs

    def set_lazy(self, i, v):
        # bgn = perf_counter()

        lazy = self.lazy
        composition = self.composition

        if lazy[i] is None:
            lazy[i] = v
        else:
            lazy[i] = composition(lazy[i], v)

        # self.t_set_lazy += perf_counter() - bgn
        # self.c_set_lazy += 1

    def resolve3(self, i):
        bgn = perf_counter()

        v = self.lazy[i]
        data = self.data

        if v is not None:
            if i < self.M:
                j = i << 1
                self.set_lazy(j, v)
                self.set_lazy(j + 1, v)

            data[i] = self.mapping(data[i], v, self.seglength[i])
            self.lazy[i] = None

        self.t_resolve += perf_counter() - bgn
        self.c_resolve += 1

    def resolve(self, i):
        # bgn = perf_counter()

        v = self.lazy[i]

        if v is not None:
            lazy = self.lazy

            if i < self.M:
                j = i << 1
                k = j | 1
                lazyj = lazy[j]
                lazyk = lazy[k]
                composition = self.composition
                lazy[j] = v if lazyj is None else composition(lazyj, v)
                lazy[k] = v if lazyk is None else composition(lazyk, v)
                # self.set_lazy(j, v)
                # self.set_lazy(j + 1, v)

            data = self.data
            data[i] = self.mapping(data[i], v, self.seglength[i])
            # self.lazy[i] = None
            lazy[i] = None

        # self.t_resolve += perf_counter() - bgn
        # self.c_resolve += 1

    def ancestors(self, segs):
        # bgn = perf_counter()

        ancestors = set()
        for i in segs:
            while i > 1:
                i >>= 1
                if i in ancestors:
                    break
                ancestors.add(i)

        # self.t_ancestors += perf_counter() - bgn
        # self.c_ancestors += 1

        return sorted(list(ancestors))

    def update2(self, qbgn, qend, value):
        set_lazy = self.set_lazy
        resolve = self.resolve
        data = self.data
        function = self.function

        segs, ancestors, others = self.segments(qbgn, qend)
        # ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            resolve(i)

        for i in others:
            resolve(i)

        for i in reversed(ancestors):
            j = i << 1
            # resolve(j)
            # resolve(j + 1)
            data[i] = function(data[j], data[j + 1])

    def update(self, qbgn, qend, v):
        # bgn = perf_counter()

        set_lazy = self.set_lazy
        lazy = self.lazy
        composition = self.composition
        resolve = self.resolve
        data = self.data
        function = self.function

        segs = self.segments(qbgn, qend)
        ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            lazyi = lazy[i]
            lazy[i] = v if lazyi is None else composition(lazyi, v)
            # set_lazy(i, value)

        for i in reversed(ancestors):
            j = i << 1
            resolve(j)
            resolve(j + 1)
            data[i] = function(data[j], data[j + 1])

        # self.t_update += perf_counter() - bgn
        # self.c_update += 1

    def query2(self, qbgn, qend):
        resolve = self.resolve
        function = self.function
        data = self.data

        segs, ancestors, _ = self.segments(qbgn, qend)
        # ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            resolve(i)

        retval = data[segs[0]]
        for i in segs[1:]:
            retval = function(retval, data[i])

        return retval

    def query(self, qbgn, qend):
        # bgn = perf_counter()

        resolve = self.resolve
        function = self.function
        data = self.data

        segs = self.segments(qbgn, qend)
        ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            resolve(i)

        retval = data[segs[0]]
        for i in segs[1:]:
            retval = function(retval, data[i])

        # self.t_query += perf_counter() - bgn
        # self.c_query += 1

        return retval

    def query_all(self):
        self.resolve(1)
        return self.data[1]

    def __str__(self):
        s = []
        for l in range(self.L):
            s.append("{:2d} {}".format(l, self.data[1 << l : 2 << l]))
        return "\n".join(s)


# update
# 0. 区間をsegmentsに分解する
# 1. segmentsのすべての祖先ノードのlazy値を（上のレイヤーから順に）消化する
# 2. segmentsの各ノードにlazy値をセットする
# 4. segmentsのすべての祖先ノードの子ノードのlazy値を消化する
# 4. segmentsのすべての祖先ノードのdata値を（下のレイヤーから順に）更新する

# query
# 0. 区間をsegmentsに分解する
# 1. segmentsのすべての祖先ノードのlazy値を（上のレイヤーから順に）消化する
# 2. segmentsの各ノードのlazy値を消化する
# 3. segmentsの各ノードのdata値を合成して返す
