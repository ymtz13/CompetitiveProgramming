memo = {}

def f(n, k, N):
  if n==0: return 1 if k>0 else 0
  if k>=9**n: return 10**n
  
  key = k*20+n
  if key in memo: return memo[key]

  retval = 10**(n-1) if n<N else 0
  for d in range(9, 0, -1):
    retval += f(n-1, k//d, N)
  print(n, k, retval)

  memo[key] = retval
  return retval

print(f(2, 1, 2))

N, K = map(int, input().split())
X = list(map(int, str(N+1)))
D = len(X)

# for check
check = 0
for n in range(1, N+1):
  s = list(map(int, str(n)))
  prod = 1
  for c in s: prod *= c
  if prod <= K: check+=1
print('check', check)

r = 1
ans = 0
for i, x in enumerate(X):
  n = D-i-1
  if r==0: 
    ans += 10**n
    break

  if i==0:
    ans += f(n, K, n)
    print('hoge', ans)
  if i>0 and x>0: ans += 10**n
  for v in range(1, x):
    ans += f(n, K//r//v, n)

  r *= x

print(ans-1)
