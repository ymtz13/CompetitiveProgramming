memo = {}

def dfs(n, m):
  if n == 0: return 0
  if m == 0: return 0

  key = (n, m)
  if key in memo: return memo[key]

  retval = 0
  # [1] 正解を当てる
  p1 = 1 / m
  c1 = 1 + dfs(n - 1, m - 1)

  # [2] 正解ではないが、あとで使う文字を当てる
  p2 = (n - 1) / m
  c2 = 3 + dfs(n - 1, m - 1)

  # [3] 正解ではなく、あとで使わない文字を当てる
  p3 = 1 - p1 - p2
  c3 = 2 + dfs(n, m - 1)

  retval = p1 * c1 + p2 * c2 + p3 * c3
  memo[key] = retval

  return retval


#n, m = map(int, input().split())
#print(dfs(n, m))
#exit()

S = input()
K = input()
ans0 = 0
for i, c in enumerate(S):
  if c in K or c in S[:i]:
    ans0 += 1

n0 = len(S) - ans0
m0 = 36 - len(K)

ans = ans0 + dfs(n0, m0)
print(ans)
