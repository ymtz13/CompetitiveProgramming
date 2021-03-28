P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
N = int(input())
X = list(map(int, input().split()))

INF = 10**202

def dfs(i, L):
  if i==len(P):
    for x in X:
      ok = False
      for p in L:
        if x%p==0:
          ok = True
          break

      if not ok: return INF
    
    prod = 1
    for p in L: prod *= p
    return prod

  p = P[i]
  return min(dfs(i+1, L), dfs(i+1, L + [p]))


print(dfs(0, []))
