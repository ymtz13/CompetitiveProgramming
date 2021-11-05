A, B, K = map(int, input().split())

F = [1]
for i in range(1, 61):
  F.append(F[-1] * i)

def dfs(a, b, k):
  if k == 1 and a+b==1: return 'a' if a==1 else 'b', None

  total = F[a+b]//F[a]//F[b]
  if total < k: return None, total
  
  if a > 0:
    ans, count = dfs(a-1, b, k)
    if ans is not None: return 'a' + ans, None
  else:
    count = 0

  ans, count = dfs(a, b-1, k - count)
  return 'b' + ans, None

print(dfs(A, B, K)[0])
