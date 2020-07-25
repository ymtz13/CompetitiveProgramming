H, W, K = map(int, input().split())
C = [input() for _ in range(H)]
ans = 0
for r in range(1<<H):
    for c in range(1<<W):
        k = 0
        for h in range(H):
            if (r>>h)&1: continue
            for w in range(W):
                if (c>>w)&1: continue
                if C[h][w]=='#': k+=1
        if k==K: ans+=1
        
print(ans)
