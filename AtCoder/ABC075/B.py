from itertools import product

H, W = list(map(int, input().split()))
S = [[0]*(W+2)] + [[0] + list(input()) + [0] for _ in range(H)] + [[0]*(W+2)]
D = list(product([-1,0,1], repeat=2))

for h, w in product(range(1,H+1), range(1,W+1)):
    if S[h][w]!='.' : continue
    n = 0
    for dx, dy in D:
        if S[h+dy][w+dx]=='#': n+=1
    S[h][w] = str(n)

for s in S[1:-1]:
    print(''.join(s[1:-1]))
