from lazy_segtree import LazySegTree
from random import randint, seed
from time import perf_counter

seed(0)


def dumb(_):
    return


def test_add_sum(print=print):
    class Naive:
        def __init__(self, N):
            self.data = [0] * N

        def update(self, qbgn, qend, value):
            for i in range(qbgn, qend):
                self.data[i] += value

        def query(self, qbgn, qend):
            return sum(self.data[qbgn:qend])

    def function(ldata, rdata):
        return ldata + rdata

    def mapping(data, lazy, seglength):
        return data + lazy * seglength

    def composition(lazy0, lazy1):
        return lazy0 + lazy1

    N = 500
    stree = LazySegTree(N, 0, function, mapping, composition)
    naive = Naive(N)

    for _ in range(100000):
        t = randint(0, 1)
        qbgn = randint(0, N - 1)
        qend = randint(qbgn + 1, N)

        if t == 0:
            vstree = stree.query(qbgn, qend)
            vnaive = naive.query(qbgn, qend)

            print(f"Query : [{qbgn}, {qend}) -> stree={vstree}, naive={vnaive}")

            assert vstree == vnaive
        else:
            v = randint(-100, 100)
            print(f"Update: [{qbgn}, {qend}) <- {v}")

            stree.update(qbgn, qend, v)
            naive.update(qbgn, qend, v)


def test_add_max(print=print):
    class Naive:
        def __init__(self, N):
            self.data = [0] * N

        def update(self, qbgn, qend, value):
            for i in range(qbgn, qend):
                self.data[i] += value

        def query(self, qbgn, qend):
            return max(self.data[qbgn:qend])

    def function(ldata, rdata):
        return max(ldata, rdata)

    def mapping(data, lazy, seglength):
        return data + lazy

    def composition(lazy0, lazy1):
        return lazy0 + lazy1

    N = 500
    stree = LazySegTree(N, 0, function, mapping, composition)
    naive = Naive(N)

    for _ in range(100000):
        t = randint(0, 1)
        qbgn = randint(0, N - 1)
        qend = randint(qbgn + 1, N)

        if t == 0:
            vstree = stree.query(qbgn, qend)
            vnaive = naive.query(qbgn, qend)

            print(f"Query : [{qbgn}, {qend}) -> stree={vstree}, naive={vnaive}")

            assert vstree == vnaive
        else:
            v = randint(-100, 100)
            print(f"Update: [{qbgn}, {qend}) <- {v}")

            stree.update(qbgn, qend, v)
            naive.update(qbgn, qend, v)


def test_set_max(print=print):
    class Naive:
        def __init__(self, N):
            self.data = [0] * N

        def update(self, qbgn, qend, value):
            for i in range(qbgn, qend):
                self.data[i] = value

        def query(self, qbgn, qend):
            return max(self.data[qbgn:qend])

    def function(ldata, rdata):
        return max(ldata, rdata)

    def mapping(data, lazy, seglength):
        return lazy

    def composition(lazy0, lazy1):
        return lazy1

    N = 500
    stree = LazySegTree(N, 0, function, mapping, composition)
    naive = Naive(N)

    for _ in range(100000):
        t = randint(0, 1)
        qbgn = randint(0, N - 1)
        qend = randint(qbgn + 1, N)

        if t == 0:
            vstree = stree.query(qbgn, qend)
            vnaive = naive.query(qbgn, qend)

            print(f"Query : [{qbgn}, {qend}) -> stree={vstree}, naive={vnaive}")

            assert vstree == vnaive
        else:
            v = randint(-100, 100)
            print(f"Update: [{qbgn}, {qend}) <- {v}")

            stree.update(qbgn, qend, v)
            naive.update(qbgn, qend, v)


test_add_sum(print=dumb)
test_add_max(print=dumb)
test_set_max(print=dumb)
