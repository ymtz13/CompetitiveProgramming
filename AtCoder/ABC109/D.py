H, W = list(map(int, input().split()))
A = [list(map(lambda c : int(c)%2, input().split())) for _ in range(H)]

ops = []
for r in range(H):
    pair_list = []
    pair_left = None
    for c in range(W):
        if A[r][c]==1:
            if pair_left!=None: pair_list.append((pair_left, c))
            pair_left = None if pair_left!=None else c

    if pair_left!=None and r!=H-1:
        ops.append((r+1, pair_left+1, r+2, pair_left+1))
        A[r+1][pair_left] += 1
        A[r+1][pair_left] %= 2

    for pair_left, pair_right in pair_list:
        for c_ in range(pair_left, pair_right):
            ops.append((r+1, c_+1, r+1, c_+2))

print(len(ops))
for op in ops:
    print(*op)
