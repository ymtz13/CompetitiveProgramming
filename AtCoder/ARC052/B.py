from math import pi

N, Q = map(int, input().split())
XRH = [tuple(map(int, input().split())) for _ in range(N)]

for q in range(Q):
  A, B = map(int, input().split())

  ans = 0
  for X, R, H in XRH:
    if X+H<A or B<X: continue

    if X<A:
      Ha = X+H-A
      Ra = R*Ha/H
      ans += Ra*Ra*Ha
    else:
      ans += R*R*H
    
    if X+H>B:
      Hb = X+H-B
      Rb = R*Hb/H
      ans -= Rb*Rb*Hb

  print(ans*pi/3)