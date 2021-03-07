A, B = input().split()

def diff(s1, s2):
  r = 0
  for c1, c2 in zip(s1, s2):
    if c1!=c2: r+=1
  return r

ans = -1000

for sa in range(100, 1000):
  if diff(A, str(sa))>1: continue
  ans = max(ans, sa - int(B))

for sb in range(100, 1000):
  if diff(B, str(sb))>1: continuek
  ans = max(ans, int(A) - sb)

print(ans)
