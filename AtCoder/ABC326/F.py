def ans(s=False):
    if not s:
        print("No")
    else:
        print("Yes")
        print(s)
    exit()


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    if X == 0 and Y == A[0]:
        ans("L")
    if X == 0 and Y == -A[0]:
        ans("R")
    ans()


A0 = A[0::2]
A1 = A[1::2]


F = 1 << 22


def listup(A):
    Rs = [0]
    Rx = [0]

    for i, a in enumerate(A):
        RsNext = []
        RxNext = []

        for rs, rx in zip(Rs, Rx):
            RsNext.append(rs + a)
            RxNext.append(rx + (1 << i))
            RsNext.append(rs - a)
            RxNext.append(rx)

        Rs = RsNext
        Rx = RxNext

    Z = [rs * F + rx for rs, rx in zip(Rs, Rx)]
    Z.sort()

    Rs = []
    Rx = []
    for z in Z:
        Rs.append(z // F)
        Rx.append(z % F)

    return Rs, Rx


def solve(A, X):
    if len(A) == 1:
        if A[0] == X:
            return [+1]
        if A[0] == -X:
            return [-1]
        return False

    N = len(A)
    AL = A[: N // 2]
    AR = A[N // 2 :]

    B = tuple(1 << i for i in range(N // 2 + 2))

    SL, XL = listup(AL)
    SR, XR = listup(AR)

    SR.reverse()
    XR.reverse()
    SR.append(-(1 << 60))
    XR.append(None)

    i = 0
    for sl, xl in zip(SL, XL):
        xx = X - sl
        while SR[i] > xx:
            i += 1
        sr = SR[i]
        xr = XR[i]

        if sl + sr == X:
            bl = [1 if xl & b else -1 for b in B[: len(AL)]]
            br = [1 if xr & b else -1 for b in B[: len(AR)]]
            return bl + br

    return False


x0 = solve(A0, Y)
x1 = solve(A1, X)

# print(x0)
# print(x1)

if not x0 or not x1:
    ans()

# VX = VY = 0
dprev = 1
anss = []
for i, a in enumerate(A):
    j = i // 2

    if i % 2 == 0:
        d = x0[j]
        anss.append("L" if d == dprev else "R")
        # VY += d * a

    else:
        d = x1[j]
        anss.append("R" if d == dprev else "L")
        # VX += d * a

    dprev = d

    # print(VX, VY)

ans("".join(anss))
