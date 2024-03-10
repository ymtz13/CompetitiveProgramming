from lazy_segtree import LazySegTree
from random import randint, seed
from time import perf_counter

seed(0)


def test_add_sum():
    def function(ldata, rdata):
        return ldata + rdata

    def mapping(data, lazy, seglength):
        return data + lazy * seglength

    def composition(lazy0, lazy1):
        return lazy0 + lazy1

    N = 1000000
    stree = LazySegTree(N, 0, function, mapping, composition)

    for _ in range(100000):
        t = randint(0, 1)
        qbgn = randint(0, N - 1)
        qend = randint(qbgn + 1, N)

        if t == 0:
            stree.query(qbgn, qend)
        else:
            v = randint(-100, 100)
            stree.update(qbgn, qend, v)


def timing(test):
    bgn = perf_counter()
    test()
    end = perf_counter()
    return end - bgn


print(timing(test_add_sum))
