import numpy as np

H, W, A, B = map(int, input().split())

S = np.zeros((H, W), int)

def dfs(i, S, a, b):
  h = i//W
  w = i%W
  if h==H:
    return 1

  if S[h, w] > 0:
    return dfs(i+1, S, a, b)
  
  retval = 0
  if b > 0:
    s = S.copy()
    s[h, w] = 1
    retval += dfs(i+1, s, a, b-1)
  
  if h < H-1 and a > 0:
    s = S.copy()
    s[h: h+2, w] = 2
    retval += dfs(i+1, s, a-1, b)

  if w < W-1 and a > 0:
    s = S.copy()
    s[h, w: w+2] = 3
    retval += dfs(i+1, s, a-1, b)
  
  return retval
  
print(dfs(0, S, A, B))
