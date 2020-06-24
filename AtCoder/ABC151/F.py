N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 100000000

for i in range(N):
    ax, ay = XY[i]
    
    for j in range(i+1, N):
        bx, by = XY[j]

        dx = (ax+bx)/2
        dy = (ay+by)/2
        r2 = (ax-dx)**2 + (ay-dy)**2

        ok = True
        for x,y in XY:
            if (x-dx)**2 + (y-dy)**2 > r2 + 1e-5:
                ok = False
                break
        if ok:
            ans = min(ans, r2)

        
        for k in range(j+1, N):
            cx, cy = XY[k]

            a = (bx-cx)**2 + (by-cy)**2
            b = (cx-ax)**2 + (cy-ay)**2
            c = (ax-bx)**2 + (ay-by)**2

            aa = a*(b+c-a)
            bb = b*(c+a-b)
            cc = c*(a+b-c)
            delim = aa + bb + cc
            if delim<1e-10: continue
            dx = (ax*aa + bx*bb + cx*cc) / delim
            dy = (ay*aa + by*bb + cy*cc) / delim
            r2 = (ax-dx)**2 + (ay-dy)**2
            

            ok = True
            for x,y in XY:
                if (x-dx)**2 + (y-dy)**2 > r2 + 1e-5:
                    ok = False
                    break
            if ok:
                ans = min(ans, r2)

print(ans**0.5)
