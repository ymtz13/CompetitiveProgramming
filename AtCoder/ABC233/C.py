N, X = map(int, input().split())
A = [list(map(int, input().split()))[1:] for _ in range(N)]

Z = [1]

for AA in A:
  Znext = []
  for z in Z:
    Znext.extend([z * a for a in AA])
  Z = Znext

print(Z.count(X))
