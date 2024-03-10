K, G, M = map(int, input().split())

xG = xM = 0

for _ in range(K):
    if xG == G:
        xG = 0
    elif xM == 0:
        xM = M
    else:
        v = min(xM, G - xG)
        xG += v
        xM -= v

print(xG, xM)
