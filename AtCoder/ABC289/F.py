M = 1000000

sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
xL, xR, yL, yR = map(int, input().split())

if (sx + tx) & 1 or (sy + ty) & 1:
    print("No")
    exit()

if sx == tx and sy == ty:
    print("Yes")
    exit()


def flip(p, p0):
    return 2 * p0 - p


A = [(sx, sx, sy, sy)]
ok = False

for _ in range(M):
    uxL, uxR, uyL, uyR = A[-1]

    vxL = 2 * xL - uxR
    vxR = 2 * xR - uxL
    vyL = 2 * yL - uyR
    vyR = 2 * yR - uyL

    A.append((vxL, vxR, vyL, vyR))

    if vxL <= tx <= vxR and vyL <= ty <= vyR:
        ok = True
        break

if not ok:
    print("No")
    exit()


A.reverse()
T = [(tx, ty)]
O = []

for b in A[1:]:
    tx, ty = T[-1]

    bxL, _, byL, _ = b

    x0 = 2 * xL - bxL
    y0 = 2 * yL - byL

    cx = bxL + max(0, x0 - tx)
    cy = byL + max(0, y0 - ty)

    T.append((cx, cy))

    ox = (tx + cx) // 2
    oy = (ty + cy) // 2

    O.append((ox, oy))

print("Yes")
for ox, oy in reversed(O):
    print(ox, oy)
