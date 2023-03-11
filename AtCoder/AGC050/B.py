N = int(input())
A = [int(input()) for _ in range(N)]

S = [0]
for a in A:
  S.append(S[-1] + a)


memo = {}

def solve(l, r, b):
  key = (l, r, b)
  if key in memo: return memo[key]

  if b==0:
    retval = 0
    for ll in range(l, r):
      for rr in range(ll+3, r, 3):
        retval = max(retval, solve(ll, rr, 1) + solve(rr, r, 0))
  
  if b==1:
    retval = S[r] - S[l]
    for ll in range(l+1, r):
      for rr in range(ll+3, r, 3):
        
        retval = max(retval, )

  s = 0 if b == 0 else S[r] - S[l]
  retval = s

  for ll in range(l+1, r):
    for rr in range(ll+3, r, 3):
      pass


  memo[key] = retval
  return retval


ans = solve(0, N, 0)
print(ans)
