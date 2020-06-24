import math

A, B, H, M = map(int, input().split())

hangle = 2*math.pi/360*(H*30+M/2)
mangle = 2*math.pi/360*M*6

hx = A*math.cos(hangle)
hy = A*math.sin(hangle)
mx = B*math.cos(mangle)
my = B*math.sin(mangle)

dx = hx-mx
dy = hy-my
d2 = dx*dx+dy*dy
d = d2**0.5
print(d)
