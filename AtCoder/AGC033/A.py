H, W = [int(c) for c in input().split()]
A = [[c=='#' for c in input()] for row in range(H)]

black_edge = []
for irow in range(H):
    for icol in range(W):
        if A[irow][icol]: black_edge.append((irow,icol))

n_black = len(black_edge)
n_operation=0
n_cell=H*W
while True:
    if n_black==n_cell: break

    n_operation+=1
    black_edge_new = []
    for irow, icol in black_edge:
        if irow-1>=0 and not A[irow-1][icol]:
            black_edge_new.append((irow-1,icol))
            A[irow-1][icol]=True
            n_black+=1
        if irow+1<H and not A[irow+1][icol]:
            black_edge_new.append((irow+1,icol))
            A[irow+1][icol]=True
            n_black+=1
        if icol-1>=0 and not A[irow][icol-1]:
            black_edge_new.append((irow,icol-1))
            A[irow][icol-1]=True
            n_black+=1
        if icol+1<W and not A[irow][icol+1]:
            black_edge_new.append((irow,icol+1))
            A[irow][icol+1]=True
            n_black+=1

    black_edge = black_edge_new

print(n_operation)
