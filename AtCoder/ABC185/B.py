N, M, T = map(int, input().split())
v = N
t = 0
for _ in range(M):
  A, B = map(int, input().split())
  v -= A - t
  if v <= 0:
    print('No')
    exit()
  v += B - A
  v = min(N, v)
  t = B

v -= T - t
if v <= 0:
  print('No')
  exit()
print('Yes')