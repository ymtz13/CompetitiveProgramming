from math import atan, sin, cos, pi

A, B = map(int, input().split())
N = int(input())

def solve(H, W, C, D):
  C, D = max(C, D), min(C, D)

  if C<=H and D<=W: return True
  if D<=H and C<=W: return True

  T = atan(D/C)

  fh = lambda x: C*cos(x) + D*sin(x)
  fw = lambda x: C*sin(x) + D*cos(x)

  if fh(pi/2-T)>H+0.005: return False

  ng = T
  ok = pi/2 - T
  while ok-ng>1e-6:
    tgt = (ok+ng)/2
    if fh(tgt)>H+0.005: ng = tgt
    else: ok = tgt

  return fw(ok)<= W    


for _ in range(N):
  C, D = map(int, input().split())
  print('YES' if solve(C, D, A, B) or solve(C, D, B, A) else 'NO')
