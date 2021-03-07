N = int(input())
P = list(map(int, input().split()))

def pans(v):
  print(v)
  exit()

ans = []

t = 0
while t<N-1:
  if P[t]==t+1: pans(-1)
  found = False
  for s in range(t+1, N):
    if P[s]==t+1: 
      P[t+1:s+1] = P[t:s]
      P[t] = t+1
      found = True
      ans += list(range(s, t, -1))
      break
  
  if not found: pans(-1)
  t = s

for t in range(N):
  if P[t] != t+1: pans(-1)

for a in ans:
  print(a)