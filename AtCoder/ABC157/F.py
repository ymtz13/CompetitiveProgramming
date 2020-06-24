N, K = map(int, input().split())
XYC = [list(map(int, input().split())) for _ in range(N)]

def f(X, Y):
    i_max = -1
    d2_max = 0
    
    for i in range(N):
        x, y, c = XYC[i]
        dx = x-X
        dy = y-Y
        d2 = c*c*(dx*dx+dy*dy)
        if d2_max<d2:
            d2_max = d2
            i_max = i

    x, y, c = XYC[i_max]
    dx = x-X
    dy = y-Y
    return dx, dy, d2_max

r = 1-1e-4
d = 1.0
X, Y = 0, 0
for _ in range(100000):
    dx, dy, d2 = f(X, Y)
    X += d*dx
    Y += d*dy
    d *= r
    if _%100==0: print('{:.5e} {:.5e}'.format(X, Y))

print(d2**0.5)
