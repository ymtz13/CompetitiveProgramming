T = int(input())
for _ in range(T):
  X, Y, P, Q = map(int, input().split())

  M = m = 2*(X+Y)
  N = n = P+Q
  K = []
  while n:
    K.append(m//n)
    r = m%n
    m, n = n, r
  gcd = m

  #print(M, N, K, gcd)

  x = v = 1
  y = u = 0
  for k in K:
    x, y, u, v = u, v, x-k*u, y-k*v
  #print(x, y)

  a = N//gcd
  b = M//gcd

  ans = INF = 10**20

  for C in range(X, X+Y):
    for D in range(P, P+Q):
      if (D-C)%gcd > 0: continueaad
      q = (D-C)//gcd

      n = x*q
      m = y*q

      if n<0:
        j = ((-n)+a-1)//a
        n += a*j
        m -= b*j

      if n>=0:
        j = n//a
        n -= a*j
        m += b*j
      
      if m>0:
        j = (m+b-1)//b
        n += a*j
        m -= b*j
      
      ans = min(ans, C+n*M)
  
  print(ans if ans != INF else 'infinity')







