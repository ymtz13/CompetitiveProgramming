def translate(P, dx, dy):
  return [(x + dx, y + dy) for x, y in P]

def dfs(level=7):
  if level==0:
    return [(0, 0)]

  P = dfs(level-1)
  d = 3**(level-1)
  return P + translate(P, d, 0) + translate(P, 0, -d)


ans = translate(dfs(), 0, 100000)

s1 = set()
s2 = set()
s3 = set()
s4 = set()

print(len(ans))
for x, y in ans:
  print(x, y)
  s1.add(y)
  s2.add(x-y)
  s3.add(x)
  s4.add(x+y)

print(len(s1), len(s2), len(s3),len(s4))
