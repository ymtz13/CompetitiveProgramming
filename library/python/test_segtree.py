from time import time
from random import seed, randrange, randint
seed(1234)

from segtree import SegTree

N = 2*10**5
fill = 0
function = max
s1 = SegTree(N, fill, function)
s2 = SegTree(N, fill, function)

M = N
data_update = [(randrange(N), randint(-10**9, +10**9)) for _ in range(M)]
data_query  = []
for _ in range(M):
    ibgn = randrange(N)
    iend = randrange(ibgn+1, N+1)
    data_query.append((ibgn, iend))

time_bgn = time()
for i, value in data_update:
    s1.update(i, value)
time_end = time()
print(time_end-time_bgn)

time_bgn = time()
for i, value in data_update:
    s2.update2(i, value)
time_end = time()
print(time_end-time_bgn)

for lyr1, lyr2 in zip(s1.data, s2.data):
    for v1, v2 in zip(lyr1, lyr2):
        assert v1==v2

time_bgn = time()
for ibgn, iend in data_query:
    s1.query(ibgn, iend)
time_end = time()

print(time_end-time_bgn)

time_bgn = time()
for ibgn, iend in data_query:
    s1.query2(ibgn, iend)
time_end = time()

print(time_end-time_bgn)

time_bgn = time()
for ibgn, iend in data_query:
    s1.query3(ibgn, iend)
time_end = time()

print(time_end-time_bgn)
