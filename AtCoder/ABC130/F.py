N = int(input())

INF = 1 << 60

xP = []
x0 = []
xN = []
yP = []
y0 = []
yN = []
for _ in range(N):
    x, y, d = input().split()
    x = int(x)
    y = int(y)

    if d == "R":
        xP.append(x)
        y0.append(y)
    if d == "L":
        xN.append(x)
        y0.append(y)
    if d == "U":
        x0.append(x)
        yP.append(y)
    if d == "D":
        x0.append(x)
        yN.append(y)


def calc_t(cP, c0, cN):
    # fP(t) = cP + t
    # f0(t) = c0
    # fN(t) = cN - t
    eP = cP is not None
    e0 = c0 is not None
    eN = cN is not None
    ret = []
    if e0 and eP:
        ret.append(c0 - cP)
    if eN and e0:
        ret.append(cN - c0)
    if eN and eP:
        ret.append((cN - cP) / 2)
    return ret


xMaxP = max(xP) if xP else None  # x(t) =  t + xMaxP
xMax0 = max(x0) if x0 else None  # x(t) =      xMax0
xMaxN = max(xN) if xN else None  # x(t) = -t + xMaxN
tXMax = calc_t(xMaxP, xMax0, xMaxN)
BXMax = [v for v in ((xMaxP, 1), (xMax0, 0), (xMaxN, -1)) if v[0] is not None]

xMinP = min(xP) if xP else None  # x(t) =  t + xMinP
xMin0 = min(x0) if x0 else None  # x(t) =      xMin0
xMinN = min(xN) if xN else None  # x(t) = -t + xMinN
tXMin = calc_t(xMinP, xMin0, xMinN)
BXMin = [v for v in ((xMinP, 1), (xMin0, 0), (xMinN, -1)) if v[0] is not None]

yMaxP = max(yP) if yP else None  # y(t) =  t + yMaxP
yMax0 = max(y0) if y0 else None  # y(t) =      yMax0
yMaxN = max(yN) if yN else None  # y(t) = -t + yMaxN
tYMax = calc_t(yMaxP, yMax0, yMaxN)
BYMax = [v for v in ((yMaxP, 1), (yMax0, 0), (yMaxN, -1)) if v[0] is not None]

yMinP = min(yP) if yP else None  # y(t) =  t + yMinP
yMin0 = min(y0) if y0 else None  # y(t) =      yMin0
yMinN = min(yN) if yN else None  # y(t) = -t + yMinN
tYMin = calc_t(yMinP, yMin0, yMinN)
BYMin = [v for v in ((yMinP, 1), (yMin0, 0), (yMinN, -1)) if v[0] is not None]

T = set(tXMax + tXMin + tYMax + tYMin + [0])
T = sorted([t for t in T if t >= 0])

ans = INF

for t, u in zip(T, T[1:] + [INF]):
    AXMax = sorted([(v + t * d, d) for v, d in BXMax])
    AXMin = sorted([(v + t * d, d) for v, d in BXMin])
    AYMax = sorted([(v + t * d, d) for v, d in BYMax])
    AYMin = sorted([(v + t * d, d) for v, d in BYMin])

    vXMax, dXMax = AXMax[-1]
    vXMin, dXMin = AXMin[0]
    vYMax, dYMax = AYMax[-1]
    vYMin, dYMin = AYMin[0]

    vX = vXMax - vXMin
    dX = dXMax - dXMin
    vY = vYMax - vYMin
    dY = dYMax - dYMin

    # rx(t)   = vX + dX * t
    # ry(t)   = vY + dY * t
    # rxry(t) = (dX*dY) * t^2 + (vX*dY + vY*dX) * t + vX*vY

    a = dX * dY
    b = vX * dY + vY * dX
    c = vX * vY

    def rxry(t):
        return a * t * t + b * t + c

    V = [rxry(0), rxry(u - t)]
    if a > 0:
        p = -b / (2 * a)
        if 0 <= p <= u - t:
            V.append(rxry(p))

    ans = min(ans, *V)

print(ans)
