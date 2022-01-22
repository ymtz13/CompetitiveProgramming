from collections import defaultdict

oa = ord('a')

N = int(input())

nV = 1
V = [None]
E = [[None] * 26]
D = [[0] * 26]
Q = []

SD = defaultdict(int)

for _ in range(N):
  S = input()[::-1]
  SD[S] += 1
  x = 0
  X = [0]
  for j, c in enumerate(S):
    #if j == len(S) - 1:
    #  Q.append((x, S[-1]))

    i = ord(c) - oa
    if E[x][i] is None:
      V.append(i)
      E.append([None] * 26)
      D.append([0] * 26)
      E[x][i] = nV
      nV += 1
    x = E[x][i]
    X.append(x)

  Q.append((X[-2], V[X[-1]]))

  s = set()
  for x in reversed(X):
    v = V[x]
    for c in s:
      D[x][c] += 1
    if x > 0: s.add(v)

#for i, (vv, ee, dd) in enumerate(zip(V, E, D)):
#  DD = {chr(cc + oa): d for cc, d in enumerate(dd) if d > 0}
#  print(i, vv, list(filter(bool, ee)), DD)

#print(Q)

ans = 0
for x, c in Q:
  #print(x, c, D[x][ord(c) - oa] - 1)
  #ans += D[x][ord(c) - oa] - 1
  ans += D[x][c] - 1

for v in SD.values():
  ans -= v * (v - 1) // 2

print(ans)
