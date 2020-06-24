H, W = [int(c) for c in input().split()]
S = [input() for _ in range(H)]

dL = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
    ml = -1
    for w in range(W):
        if S[h][w]=='.':
            dL[h][w] += w-ml
        else:
            ml=w
            
    mr = W
    for w in range(W-1, -1, -1):
        if S[h][w]=='.':
            dL[h][w] += mr-w
        else:
            mr=w

for w in range(W):
    mu = -1
    for h in range(H):
        if S[h][w]=='.':
            dL[h][w] += h-mu
        else:
            mu=h
            
    md = H
    for h in range(H-1, -1, -1):
        if S[h][w]=='.':
            dL[h][w] += md-h
        else:
            md=h

max_lite = -1
for h in range(H):
    max_lite = max(max_lite, max(dL[h])-3)

for h in range(H):
    for w in range(W):
        if S[h][w]=='.':
            c = dL[h][w]-3
            if c>9: c='ABCDEFGHIJKLMN'[c-10]
        else:
            c='#'
        print(c, end='')
    print()

print(max_lite)
