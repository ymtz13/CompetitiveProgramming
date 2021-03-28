from math import tau, sin, cos

N = int(input())
x0, y0 = map(int, input().split())
xd, yd = map(int, input().split())

xc = (x0 + xd)/2
yc = (y0 + yd)/2

xH = x0 - xc
yH = y0 - yc
xV = -yH
yV = +xH

angle = tau/N

x1 = xc + xH*cos(angle) + xV*sin(angle)
y1 = yc + yH*cos(angle) + yV*sin(angle)
print(x1, y1)
