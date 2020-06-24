H, W = [int(c) for c in input().split()]
A = [[c=='#' for c in input()] for row in range(H)]

black = []
white = []
for irow in range(H):
    for icol in range(W):
        if A[irow][icol]:
            black.append((irow,icol))
        else:
            white.append((irow,icol))


dmax=0
for w_x, w_y in white:
    dmin=1000000
    for b_x, b_y in black:
        d = abs(bx-wx)+abs(by-wy)
        if d<dmin:
            dmin=d
    if dmin>dmax:
        dmax=dmin

print(dmax)
