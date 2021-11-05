def unsolvable():
  print('UNSOLVABLE')
  exit()

D = {}
S = [input() for _ in range(3)]

K = [[] for _ in range(3)]
cnt = 0
for i, s in enumerate(S):
  for j, c in enumerate(s[::-1]):
    if c not in D:
      D[c] = cnt
      cnt += 1    
    K[i].append(D[c])

if cnt>10: unsolvable()

X = [None]*cnt
R = [False]*10

def build(k):
  t = 1
  retval = 0
  for z in k:
    retval += t*X[z]
    t *= 10
  if X[z]==0: return -10**20
  return retval

def dfs(i):
  if i==cnt:
    N1 = build(K[0])
    N2 = build(K[1])
    N3 = build(K[2])
    
    if N1 + N2 == N3:
      print(N1)
      print(N2)
      print(N3)
      exit()
    
    return
  
  for v in range(10):
    if R[v]: continue
    R[v] = True
    X[i] = v
    dfs(i+1)
    R[v] = False

dfs(0)
unsolvable()
