mod = 998244353
N, K = map(int, input().split())
D = [None]*N
L = [None]*N
R = [None]*N
ans = 1

for i in range(K):
  c, k = input().split()
  k = int(k)
  if D[k-1] is not None: ans = 0
  D[k-1] = i
  if c=='L': L[k-1] = i
  if c=='R': R[k-1] = i

x = len(tuple(filter(lambda x: x is not None, R)))

for n in range(N):
  if L[n] is not None:
    x += 1
    continue
  if R[n] is not None:
    x -= 1
    continue

  ans = ans * x % mod

print(ans)
