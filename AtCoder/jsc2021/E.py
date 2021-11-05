from collections import defaultdict

K = int(input())
S = input()

if K==0:
  if len(S)==1:
    print('impossible')
  else:
    print(1 if S==S[::-1] else 0)
  exit()

F = [[] for _ in range(K)]

def dfs(bgn, end, k):
  if k > 0 and bgn == end:
    print('impossible')
    exit()

  L = end-bgn
  l = L//2

  if k==1:
    s = S[bgn: end]
    F[k-1].append(s[:l])
    F[k-1].append(s[::-1][:l])

  else:
    cl = dfs(bgn, bgn+l, k-1)
    cr = dfs(end-l, end, k-1)
    F[k-1].append(cl)
    F[k-1].append(cr)

  return '' if L%2==0 else S[bgn + l]

dfs(0, len(S), K)
#print(F)

f = F[0]
lenf = len(f)
L = len(f[0])
if L==1:
  print('impossible')
  exit()

C = [defaultdict(int) for _ in range(L)]
for f in F[0]:
  for i, x in enumerate(f): C[i][x] += 1

cost = 0
maxstr = []
secondmin = lenf
for i, c in enumerate(C):
  rank = sorted([(v, k) for k, v in c.items()], reverse=True)
  #print(i, rank)
  first = rank[0]
  cost += lenf - first[0]
  maxstr.append(first[1])
  if len(rank) > 1 and not (L%2==1 and i==L//2):
    secondmin = min(secondmin, first[0] - rank[1][0])
    #print(i, first, rank[1], first[0]-rank[1][0])

#print(cost, secondmin)

maxstr = ''.join(maxstr)
if len(maxstr) > 0 and maxstr==maxstr[::-1]:
  cost += secondmin

#print(cost, maxstr)

for f in F[1:]:
  C = defaultdict(int)
  for c in f: C[c] += 1
  cost += len(f) - max(C.values())

print(cost)
