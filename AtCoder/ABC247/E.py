N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

b = []
B = []
for a in A + [-1]:
  if (a > X or a < Y):
    if b:
      B.append(b)
      b = []

  else:
    b.append(a)

ans = 0
for A in B:
  ix = iy = None
  for i, a in enumerate(A, 1):
    if a == X: ix = i
    if a == Y: iy = i
    if ix is None or iy is None: continue
    ans += min(ix, iy)

print(ans)
