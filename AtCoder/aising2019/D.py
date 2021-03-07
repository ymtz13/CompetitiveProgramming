from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
Se = []
So = []
s = se = so = 0
for i, a in enumerate(A):
  s += a
  if i%2==0: se += a
  else: so += a
  S.append(s)
  Se.append(se)
  So.append(so)

for _ in range(Q):
  x = int(input())

  if A[-1]>=x:
    ng = bisect_left(A, x)-1
    ok = N-1
    while ok-ng>1:
      tgt = (ok+ng)//2
      v = A[tgt]
      d = v - x
      s = bisect_left(A, x-d)
      t = bisect_left(A, v+1)
      n = t-s
      #print('{} items exist between [{}, {}]'.format(n, x-d, v))
      #print('bb', tgt, v, s, t, n )
      if N-tgt<=n: ok = tgt
      else: ng = tgt
  
  else:
    ok = N-1
  
  ans = S[N] - S[ok]

  k = N - ok
  j = N - k*2 - 1
  #print(ok, k, j)
  if j>=0:
    ans += Se[j] if j%2==0 else So[j]
  print(ans)
