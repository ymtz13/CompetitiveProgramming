def test1():
  N = 10
  E = []
  for i in range(1, N+1):
    for j in range(i+1, N+1):
      E.append((i, j))

  return N, E

def test2():
  N = 2*(10**5)
  E = []
  for i in range(2, N+1):
    E.append((i-1, i))

  return N, E


N, E = test1()
M = len(E)
print(N, M)
for e in E:
  print(*e)

