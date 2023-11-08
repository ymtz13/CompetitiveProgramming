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

    SL = []
    SR = []

    for x in range(1 << len(AL)):
        v = [a if x & b else -a for b, a in zip(B, AL)]
        SL.append((sum(v), x))

    for x in range(1 << len(AR)):
        v = [a if x & b else -a for b, a in zip(B, AR)]
        SR.append((sum(v), x))

    SL.sort()
    SR.sort(reverse=True)
    SR.append((-(1 << 60), None))

    i = 0
    for sl, xl in SL:
        while SR[i][0] + sl > X:
            i += 1
        sr, xr = SR[i]

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
