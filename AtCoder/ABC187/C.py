N = int(input())
S = [input() for _ in range(N)]

T = set()
F = set()

for s in S:
  if s[0]=='!': F.add(s[1:])
  else: T.add(s)

for t in T:
  if t in F:
    print(t)
    exit()

print('satisfiable')
