N = int(input())

ans = []
def dfs(S, C):
  if len(S)==N:
    print(S)
    return

  for c in range(ord('a'), C+2):
    dfs(S+chr(c), max(c, C))

dfs('a', ord('a'))
