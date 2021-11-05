N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]

def check(V):
  dp = [[1] + [0]*31 for _ in range(4)]
  for status in S:
    b = 0
    for i, s in enumerate(status):
      if s>=V: b += 1<<i
    
    for n in (3, 2, 1):
      for j in range(32):
        dp[n][j|b] |= dp[n-1][j]

  return dp[3][31]

ng = 10**10
ok = 0
while ng-ok>1:
  tgt = (ng+ok)//2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
