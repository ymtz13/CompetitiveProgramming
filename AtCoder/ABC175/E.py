R, C, K = map(int, input().split())

V = [[0]*(C+1) for _ in range(R+1)]
dp1 = [[0,0,0,0] for _ in range(C+1)]

for _ in range(K):
    r, c, v = map(int, input().split())
    V[r][c] = v

for r in range(1,R+1):
    dp0 = dp1
    dp1 = [[0,0,0,0] for _ in range(C+1)]
    
    for c in range(1,C+1):
        v = V[r][c]
        dprc  = dp1[c]
        dprcL = dp1[c-1]
        if v==0:
            dprc[0] = max(max(dp0[c]), dprcL[0])
            for n in range(1,4): dprc[n] = dprcL[n]
        else:
            maxT = max(dp0[c])
            dprc[0] = max(maxT  ,             dprcL[0])
            dprc[1] = max(maxT+v, dprcL[0]+v, dprcL[1])
            dprc[2] = max(        dprcL[1]+v, dprcL[2])
            dprc[3] = max(        dprcL[2]+v, dprcL[3])
        

print(max(dp1[C]))
