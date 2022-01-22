A = tuple(map(int, input()))
B = tuple(map(int, input()))

rev = False
if len(A) < len(B):
  A, B = B, A
  rev = True

Ca0 = [0] * 10
Cb0 = [0] * 10
for a in A:
  Ca0[a] += 1
for b in B:
  Cb0[b] += 1

Ca0[0] = max(0, len(B) - len(A))
Cb0[0] = max(0, len(A) - len(B))

ans = (0, A, B)

for a0, ca in enumerate(Ca0):
  if ca == 0: continue
  for b0, cb in enumerate(Cb0):
    if a0 + b0 < 10 or cb == 0: continue

    Ca = Ca0[:]
    Cb = Cb0[:]
    Ca[a0] -= 1
    Cb[b0] -= 1
    ansA = []
    ansB = []

    pair = 1

    for da in range(9, -1, -1):
      for db in range(9 - da, 10):
        x = min(Ca[da], Cb[db])
        Ca[da] -= x
        Cb[db] -= x
        ansA.extend([da] * x)
        ansB.extend([db] * x)
        pair += x

    ansA.append(a0)
    ansB.append(b0)

    ansPA = []
    ansPB = []
    for d in range(10):
      ansPA.extend([d] * Ca[d])
      ansPB.extend([d] * Cb[d])
    n0 = Cb[0]

    ansA = ansPA[:n0] + ansA + ansPA[n0:]
    ansB = ansPB[:n0] + ansB + ansPB[n0:]

    #print(ansA)
    #print(ansB)
    #print(pair)
    #print()

    if pair > ans[0]:
      ans = (pair, ansA, ansB)

    break

pair, ansA, ansB = ans

aA = ''.join(map(str, ansA))
aB = ''.join([str(c) if c else '' for c in ansB])
if rev: aA, aB = aB, aA
print(aA)
print(aB)
