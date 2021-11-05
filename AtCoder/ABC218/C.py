N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def getFigure(X):
  sh = sw = None
  retval = []
  for h in range(N):
    for w in range(N):
      if X[h][w] == '.': continue
      if sh is None:
        sh = h
        sw = w
      retval.append((h - sh, w - sw))
  return retval


def rotate(X):
  retval = [[None]*N for _ in range(N)]
  for h in range(N):
    for w in range(N):
      retval[w][N-1-h] = X[h][w]
  return retval

fS = getFigure(S)
for i in range(4):
  if fS == getFigure(T):
    print('Yes')
    exit()
  T = rotate(T)

print('No')
