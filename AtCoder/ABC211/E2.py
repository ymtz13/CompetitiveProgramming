from collections import defaultdict

N = int(input())
K = int(input())
S = [int(''.join(map(lambda c: '1' if c=='#' else '0', input())), 2) for _ in range(N)]

print(S)

P = [None]*N

def dfs(n=0, row=0, st=False):
  if row==N:
    if n!=K: return 0

    # check UF
    print(P)
    return 1

  retval = 0
  for i in range(1<<N):
    c = bin(i).count('1')
    if st and P[row-1]&i==0: continue
    if i&S[row]>0: continue
    if n+c>K: continue

    P[row] = i
    retval += dfs(n+c, row+1, st or c>0)
    P[row] = None

  return retval

print(dfs())
