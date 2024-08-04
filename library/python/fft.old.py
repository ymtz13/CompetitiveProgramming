from cmath import exp
from math import tau

wws = {}
for i in range(1, 23):
    n = 1 << i
    k = tau / n * 1j
    ww = [exp(k * i) for i in range(n >> 1)]
    wws[n] = (ww, [w.conjugate() for w in ww])


def fft(n, aa, inverse=False):
    if n == 1:
        return aa

    aa0 = aa[0::2]
    aa1 = aa[1::2]

    nn = n >> 1
    bb0 = fft(nn, aa0, inverse)
    bb1 = fft(nn, aa1, inverse)

    # k = tau / n * (1j if inverse else -1j)
    # ww = [exp(k * i) for i in range(nn)]
    ww = wws[n][1 if inverse else 0]
    r0 = [b0 + w * b1 for b0, b1, w in zip(bb0, bb1, ww)]
    r1 = [b0 - w * b1 for b0, b1, w in zip(bb0, bb1, ww)]

    return r0 + r1


# fft(1 << 22, list(range(1 << 22)))

a = [3, 5, 10, 13]
print(fft(4, a))

a = list(range(8))
b = fft(8, a)
c = fft(8, b, inverse=True)
d = fft(8, a, inverse=True)
e = fft(8, d)

print(a)
print(b)
print(c)
print(d)
print(e)

p = [3, 8, 5, 2, 7, 4] + [0] * 10
q = [1, 9, 6, 3, 7, 1] + [0] * 10

# p = [3, 8, 0, 0, 0, 0] + [0] * 10
# q = [1, 2, 0, 0, 0, 0] + [0] * 10

fp = fft(16, p)
fq = fft(16, q)

fpq = [vp * vq for vp, vq in zip(fp, fq)]
pq = fft(16, fpq, inverse=True)

pq = [round(v.real / 16) for v in pq]
print(pq)
assert pq == [3, 35, 95, 104, 100, 153, 127, 64, 63, 35, 4, 0, 0, 0, 0, 0]
