H, W, M = map(int, input().split())
Nh = [0]*(H+1)
Nw = [0]*(W+1)
HW = []
for _ in range(M):
    h, w = map(int, input().split())
    HW.append((h,w))

    Nh[h] += 1
    Nw[w] += 1

maxH = max(Nh)
Ih = [False] * (H+1)
xh = 0
for ih, nh in enumerate(Nh):
    if nh==maxH:
        Ih[ih] = True
        xh += 1

maxW = max(Nw)
Iw = [False] * (W+1)
xw = 0
for iw, nw in enumerate(Nw):
    if nw==maxW:
        Iw[iw] = True
        xw += 1

n = 0
for ih, iw in HW:
    if Ih[ih] and Iw[iw]: n+=1

ans = maxH+maxW
print(ans if n<xh*xw else ans-1)
