N = int(input())
T = [int(input()) for _ in range(N)]

def dfs(i, s1, s2):
  if i==N: return max(s1, s2)
  return min(dfs(i+1, s1+T[i], s2), dfs(i+1, s1, s2+T[i]))

print(dfs(0, 0, 0))
