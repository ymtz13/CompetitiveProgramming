from cmath import exp
from math import tau


def fft(n, aa, inverse=False):
    m = 1
    nn = n >> 1
    taui = tau * (1j if inverse else -1j)

    while m < n:
        aanxt = []

        ww = [exp(taui * i / m / 2) for i in range(m)]

        for p0, q0 in zip(range(0, nn, m), range(nn, n, m)):
            aap = aa[p0 : p0 + m]
            aaq = aa[q0 : q0 + m]

            waaq = [w * aq for w, aq in zip(ww, aaq)]

            for ap, waq in zip(aap, waaq):
                aanxt.append(ap + waq)

            for ap, waq in zip(aap, waaq):
                aanxt.append(ap - waq)

        aa = aanxt
        m <<= 1

    return aa


def fftx(n, aa, inverse=False):
    m = 0
    while (1 << m) < n:
        m += 1

    bits = [(1 << i, 1 << (m - 1 - i)) for i in range(m)]

    bb = [None] * n
    for i, a in enumerate(aa):
        j = sum([jb for ib, jb in bits if i & ib])
        bb[j] = a

    chunk_size = 2
    while chunk_size <= n:
        chunk_size_half = chunk_size >> 1
        num_chunks = n // chunk_size

        for k in range(chunk_size_half):
            w = exp(tau * k / chunk_size * (1j if inverse else -1j))
            for ichunk in range(num_chunks):
                p = ichunk * chunk_size + k
                q = p + chunk_size_half

                vp = bb[p] + w * bb[q]
                vq = bb[p] - w * bb[q]

                bb[p] = vp
                bb[q] = vq

        chunk_size <<= 1

    return bb


fft(1 << 22, list(range(1 << 22)))


def pret(aa):
    return [round(v.real) + round(v.imag) * 1j for v in aa]


n = 8
a = list(range(n))
# a = [1, 6, 3, 6, 7, 3, 4, 6, 3, 4, 5, 8, 12, 4, 56, 12, 4, 5, 32, 21, 56, 3, 1][:16]
b = fft(n, a)
c = fft(n, b, inverse=True)
d = fft(n, a, inverse=True)
e = fft(n, d)

print("a", a)
print("b", b)
print("c", c)
print("d", d)
print("e", e)

p = [3, 8, 5, 2, 7, 4] + [0] * 10
q = [1, 9, 6, 3, 7, 1] + [0] * 10

# p = [3, 8, 0, 0, 0, 0] + [0] * 10
# q = [1, 2, 0, 0, 0, 0] + [0] * 10

fp = fft(16, p)
fq = fft(16, q)

fpq = [vp * vq for vp, vq in zip(fp, fq)]
print(fpq)
pq = fft(16, fpq, inverse=True)

pq = [round(v.real / 16) for v in pq]
print(pq)
assert pq == [3, 35, 95, 104, 100, 153, 127, 64, 63, 35, 4, 0, 0, 0, 0, 0]
