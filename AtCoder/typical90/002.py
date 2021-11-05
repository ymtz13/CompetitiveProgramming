N = int(input())

def dfs(s):
  #print(s)
  n = N - len(s)
  if n==0:
    print(s)
    return

  l = s.count('(') - s.count(')')

  if l+1 <= n-1:
    dfs(s + '(')

  if l>0:
    dfs(s + ')')

dfs('')
