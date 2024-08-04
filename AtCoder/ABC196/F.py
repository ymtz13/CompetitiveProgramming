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


S = [2 * int(c) - 1 for c in input()]
T = [2 * int(c) - 1 for c in input()][::-1]

# print(S)
# print(T)


N = 1
while N < len(S) * 2 + 10:
    N *= 2

fs = fft(N, S + [0] * (N - len(S)))
ft = fft(N, T + [0] * (N - len(T)))

fst = [vs * vt for vs, vt in zip(fs, ft)]
st = fft(N, fst, inverse=True)

st = [round(v.real / N) for v in st]

# print(st)

st = st[len(T) - 1 :][: len(S) - len(T) + 1]
# print(st)

v = max(st)

print((len(T) - v) // 2)
