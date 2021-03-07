from bisect import bisect_left

N, M = map(int, input().split())
W = list(map(int, input().split()))

LV = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x:x[1])
V = [0] # 重さV[i] 以上の部分列は
L = [0] # 長さL[i] 以上にすること
for l, v in LV:
    if V[-1]==v:
        L[-1] = max(L[-1], l)
    else:
        V.append(v)
        L.append(max(L[-1], l))

if V[1]<max(W):
    print(-1)
    exit()

used = [False]*N
order = [None]*N
loc = [0]*N
ans = 10**9

def dfs(i, loc_prev):
    if i==N:
        global ans
        #print(order, loc)
        ans = min(ans, loc_prev)
        return

    for p in range(N):
        if used[p]: continue

        used[p]=True
        order[i]=p

        w = W[p]
        loc_i = loc_prev
        for j in range(i-1, -1, -1):
            w += W[order[j]]
            l = L[bisect_left(V, w)-1]
            loc_i = max(loc_i, loc[j] + l)
            #if order==[0,2,1]: print(j, w, l, loc_i)
        loc[i] = loc_i

        dfs(i+1, loc_i)
        
        used[p]=False

dfs(0,0)
print(ans)
