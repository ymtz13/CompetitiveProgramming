N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

INF = 1 << 60

XL = []
YL = []
XR = []
YR = []
for x, y in XY:
    XL.append(x)
    YL.append(y)
    XR.append(-x)
    YR.append(-y)

XL.sort()
YL.sort()
XR.sort()
YR.sort()

SXL = sum(XL)
SYL = sum(YL)
SXR = sum(XR)
SYR = sum(YR)

XL.append(INF)
YL.append(INF)
XR.append(INF)
YR.append(INF)


def g(A, S, T):
    r = 0
    sl = sr = 0
    m = INF
    for l, a in enumerate(A[:-1]):
        while A[r] <= a + T:
            sr += A[r]
            r += 1

        cl = a * l - sl
        cr = S - sr - (a + T) * (N - r)

        # print((l, r), (sl, sr), (cl, cr), S)

        m = min(m, cl + cr)

        sl += a

    return m


# print(g(XL, SXL, 3))

# exit()


def f(T):
    xl = g(XL, SXL, T)
    xr = g(XR, SXR, T)
    yl = g(YL, SYL, T)
    yr = g(YR, SYR, T)

    # print(T, xl, xr, yl, yr)

    return min(xl, xr) + min(yl, yr) <= K


ok = 10**9
ng = -1
while ok - ng > 1:
    tgt = (ok + ng) // 2
    if f(tgt):
        ok = tgt
    else:
        ng = tgt

print(ok)
