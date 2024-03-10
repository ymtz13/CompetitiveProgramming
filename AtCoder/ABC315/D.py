H, W = map(int, input().split())
C = [input() for _ in range(H)]

XH = []
YH = []
for h in range(H):
    s = set()
    y = [0] * 26
    for w in range(W):
        c = ord(C[h][w]) - ord("a")
        s.add(c)
        y[c] += 1
    XH.append(len(s))
    YH.append(y)

XW = []
YW = []
for w in range(W):
    s = set()
    y = [0] * 26
    for h in range(H):
        c = ord(C[h][w]) - ord("a")
        s.add(c)
        y[c] += 1
    XW.append(len(s))
    YW.append(y)


def pick(y):
    for i in range(26):
        if y[i] > 0:
            return i


kH = H
kW = W

ans = 0
while True:
    iH = [(h, pick(YH[h])) for h, x in enumerate(XH) if x == 1 and kW > 1]
    iW = [(w, pick(YW[w])) for w, x in enumerate(XW) if x == 1 and kH > 1]

    for h, c in iH:
        for w in range(W):
            y = YW[w]
            y[c] -= 1
            if y[c] == 0:
                XW[w] -= 1
        XH[h] = 0

    for w, c in iW:
        for h in range(H):
            y = YH[h]
            y[c] -= 1
            if y[c] == 0:
                XH[h] -= 1
        XW[w] = 0

    nH = len(iH)
    nW = len(iW)

    cnt = nH * kW + nW * kH - nH * nW
    ans += cnt

    kH -= nH
    kW -= nW

    if cnt == 0:
        break


print(H * W - ans)
