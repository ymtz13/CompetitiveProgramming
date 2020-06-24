H, W, K = list(map(int, input().split()))
S = [input() for _ in range(H)]
nrow = [s.count('#') for s in S]
hline = [-1]+[i for i in range(H) if nrow[i]>0][:-1] + [H-1]

ans = [[None]*W for _ in range(H)]

k=1
for ihline in range(1, len(hline)):
    ncol = [0]*W
    for r in range(W):
        for ih in range(hline[ihline-1]+1, hline[ihline]+1):
            if S[ih][r]=='#': ncol[r]+=1
    vline = [-1]+[i for i in range(W) if ncol[i]>0][:-1] + [W-1]

    for ivline in range(1, len(vline)):
        for ih in range(hline[ihline-1]+1, hline[ihline]+1):
            for ir in range(vline[ivline-1]+1, vline[ivline]+1):
                ans[ih][ir] = k
        k+=1

for r in ans:
    print(*r)
