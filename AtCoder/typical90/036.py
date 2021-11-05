N, Q = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

R = [
  sorted(P, key=lambda p: +p[0]+p[1])[0],
  sorted(P, key=lambda p: +p[0]-p[1])[0],
  sorted(P, key=lambda p: -p[0]+p[1])[0],
  sorted(P, key=lambda p: -p[0]-p[1])[0],
]

for _ in range(Q):
  q = int(input())
  px, py = P[q-1]
  print(max([abs(px-rx) + abs(py-ry) for rx, ry in R]))
