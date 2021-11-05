from math import tau, sin, cos, atan

T = int(input())
L, X, Y = map(int, input().split())
l = L/2

Q = int(input())
for _ in range(Q):
  E = int(input())
  rad = tau * E / T

  y = -l*sin(rad)
  z = -l*cos(rad) + l

  dx = X
  dy = Y-y
  dist = (dx*dx + dy*dy) ** 0.5

  print(atan(z/dist)*360/tau)

