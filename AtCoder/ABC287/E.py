N = int(input())
S = [input() for _ in range(N)]

E = [{}]
P = [None]
L = [0]
X = [N]
M = 1

F = []

for k, s in enumerate(S):
  i = 0
  for l, c in enumerate(s, 1):
    e = E[i]
    if c not in e:
      E.append({})
      P.append(i)
      L.append(l)
      X.append(0)

      e[c] = M
      M += 1

    i = e[c]
    X[i] += 1

  F.append(i)

#for k, (e, p, l, x) in enumerate(zip(E, P, L, X)):
#  print(k, e, p, l, x)

for f in F:
  while X[f] == 1:
    f = P[f]
  print(L[f])
