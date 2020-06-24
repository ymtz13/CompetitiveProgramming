s = input()
x, y = list(map(int, input().split()))
F = [len(fs) for fs in s.split('T')]
x -= F[0]
Fx = F[2::2]
Fy = F[1::2]

xt2 = sum(Fx)-x
yt2 = sum(Fy)-y
if xt2%2==1 or yt2%2==1 or xt2<0 or yt2<0:
    print('No')
    exit()

xt = xt2//2
yt = yt2//2

dpx = [False]*(xt+1)
dpx[0] = True
for f in Fx:
    for i in range(xt, f-1, -1): dpx[i] |= dpx[i-f]

dpy = [False]*(yt+1)
dpy[0] = True
for f in Fy:
    for i in range(yt, f-1, -1): dpy[i] |= dpy[i-f]

print('Yes' if dpx[xt] and dpy[yt] else 'No')

