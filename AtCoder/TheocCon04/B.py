W, H, N = list(map(int,input().split()))
l, r, u, d = 0, W, H, 0
for _ in range(N):
    x, y, a = list(map(int,input().split()))
    if a==1: l = max(l,x)
    if a==2: r = min(r,x)
    if a==3: d = max(d,y)
    if a==4: u = min(u,y)
print(max(0,r-l)*max(0,u-d))
