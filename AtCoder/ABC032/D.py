N, W = map(int, input().split())
wv = []
w_max = 0
for _ in range(N):
    v, w = map(int, input().split())
    wv.append((w,v))
    w_max = max(w_max, w)

def dfs(wv, a, l, i, w, v):
    if i==l:
        if w not in a: a[w]=0
        a[w] = max(a[w], v)
        return

    if w>W: return

    wi, vi = wv[i]
    dfs(wv, a, l, i+1, w, v)
    dfs(wv, a, l, i+1, w+wi, v+vi)    

    
if N<=30:
    wvL = wv[:N//2]
    wvR = wv[N//2:]
    aL = {0:0}
    aR = {0:0}
    dfs(wvL, aL, len(wvL), 0, 0, 0)
    dfs(wvR, aR, len(wvR), 0, 0, 0)

    aL = sorted(list(aL.items()))
    aR = sorted(list(aR.items()))

    sR = []
    v_max = 0
    for w, v in aR:
        v_max = max(v_max, v)
        sR.append((w, v_max))
        
    r = len(aR)-1
    ans = 0
    for wL, vL in aL:
        while r>=0 and sR[r][0]+wL>W: r -= 1
        if r==-1: break
        ans = max(ans, sR[r][1]+vL)

elif w_max<=1000:
    dp = [0]*200001
    for w, v in wv:
        for i in range(200000, w-1, -1):
            dp[i] = max(dp[i], dp[i-w]+v)

    ans = 0
    for w in range(200001):
        if w>W: break
        ans = max(ans, dp[w])

else:
    INF = 10**12
    dp = [INF]*200001
    dp[0] = 0
    for w, v in wv:
        for i in range(200000, v-1, -1):
            dp[i] = min(dp[i], dp[i-v]+w)

    ans = 200000
    while dp[ans]>W: ans-=1

print(ans)
