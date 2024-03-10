from segtree import SegTree
from random import randint, seed

seed(0)


def dumb(_):
    return


def test_sum(print=print):
    N = 500

    class Naive:
        data = [0] * N

        def update(self, i, value):
            self.data[i] = value

        def query(self, qbgn, qend):
            return sum(self.data[qbgn:qend])

    def function(ldata, rdata):
        return ldata + rdata

    stree = SegTree(N, 0, function)
    naive = Naive()

    for _ in range(100000):
        t = randint(0, 1)

        if t == 0:
            qbgn = randint(0, N - 1)
            qend = randint(qbgn + 1, N)

            vstree = stree.query(qbgn, qend)
            vnaive = naive.query(qbgn, qend)

            print(f"Query : [{qbgn}, {qend}) -> stree={vstree}, naive={vnaive}")

            assert vstree == vnaive
        else:
            i = randint(0, N - 1)
            v = randint(-100, 100)
            print(f"Update: #{i} <- {v}")

            stree.update(i, v)
            naive.update(i, v)


def test_max(print=print):
    N = 500
    initial = [randint(-100, 100) for _ in range(N)]

    class Naive:
        data = initial[:]

        def update(self, i, value):
            self.data[i] = value

        def query(self, qbgn, qend):
            return max(self.data[qbgn:qend])

    function = max

    stree = SegTree(N, 0, function, initial)
    naive = Naive()

    for _ in range(100000):
        t = randint(0, 1)

        if t == 0:
            qbgn = randint(0, N - 1)
            qend = randint(qbgn + 1, N)

            vstree = stree.query(qbgn, qend)
            vnaive = naive.query(qbgn, qend)

            print(f"Query : [{qbgn}, {qend}) -> stree={vstree}, naive={vnaive}")

            assert vstree == vnaive
        else:
            i = randint(0, N - 1)
            v = randint(-100, 100)
            print(f"Update: #{i} <- {v}")

            stree.update(i, v)
            naive.update(i, v)


test_sum(print=dumb)
test_max(print=dumb)
