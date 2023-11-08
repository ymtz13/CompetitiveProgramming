XA, YA, XB, YB, XC, YC = map(int, input().split())

if XB > XC:
    XA = -XA
    XB = -XB
    XC = -XC

if YB > YC:
    YA = -YA
    YB = -YB
    YC = -YC


DX = XC - XB
DY = YC - YB


def initial_move(XA, YA, XB, YB, XT, YT):
    if XA == XT and YA == YT:
        return 0

    if XA > XT:
        XA = -XA
        XB = -XB
        XT = -XT

    if YA > YT:
        YA = -YA
        YB = -YB
        YT = -YT

    ret = (XT - XA) + (YT - YA)
    if XA == XT and XA == XB and YA < YB < YT:
        return ret + 2

    if YA == YT and YA == YB and XA < XB < XT:
        return ret + 2

    return ret


# x first
ans_x = 1 << 100
if DX:
    ans_x = initial_move(XA, YA, XB, YB, XB - 1, YB) + DX + DY
    if DY:
        ans_x += 2

# y first
ans_y = 1 << 100
if DY:
    ans_y = initial_move(XA, YA, XB, YB, XB, YB - 1) + DX + DY
    if DX:
        ans_y += 2

print(min(ans_x, ans_y))
