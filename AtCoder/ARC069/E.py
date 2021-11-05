N = int(input())
A = [(i + 1, a) for i, a in enumerate(map(int, input().split()))] + [(0, 0)]
A = sorted(A, key=lambda x: -x[1])

x = INF = 10**10
p = N + 1
s = 0

ans = [0] * (N + 2)
for c, (i, a) in enumerate(A):
  if i < p:
    ans[p] = c * (x - a) - s
    x = a
    p = i
    s = 0

  s += x - a

for a in ans[1:-1]:
  print(a)

#                 o
#                 o
#                 o
#               o o
#           o   o o
#       o   o   o o
#   o   o o o o o o
# o o o o o o o o o o
# 1 2 3 4 5 6 7 8 9 A