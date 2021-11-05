N, K = map(int, input().split())
M = [0] * (3*N+1)
s = 0

for x in range(3, 3*N+1):
  if   x <= N+2:
    l = x - 2
    m = l*(l+1)//2
  elif x <= 2*N+1:
    l = x - (N+2)
    m = (N+l)*(N+l+1)//2 - 3*l*(l+1)//2
  else:
    l = 3*N - x + 1
    m = l*(l+1)//2
  
  M[x] = m
  s += m
  if s < K: continue

  k = K - (s-m) + 1

  if   x <= N+2:
    l = x - 2
    t = 0
    for s1 in range(1, l+1):
      count = l - s1 + 1
      t += count
      if t >= k:
        s2 = k - (t-s1)+1
        print(s1, s2, x - s1 - s2)
        exit()

  elif x <= 2*N+1:
    l = x - (N+2)
    t = 0
    for s1 in range(1, l+2):
      count = N + l
      t += s1
      if t >= k:
        s2 = k - (t-s1)+1
      pass

    for s1 in range(l+3, N+1):
      pass

  else:
    l = 3*N - x + 1
    t = 0
    for s1 in range(N-l+1, N+1):
      t += s1 - (N-l)
      if t >= k:
        s2 = k - (t-j) + 1 + N-l
        print(s1, s2, x - s1 - s2)
        exit()

