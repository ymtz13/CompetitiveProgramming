from math import atan, pi
a, b, x = list(map(int,input().split()))
V = a*a*b/2
if x<=V:
    c = 2*x/a/b
    angle = atan(b/c)*180/pi
else:
    d = 2*x/a/a - b
    angle = atan((b-d)/a)*180/pi
print(angle)
