from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Da = defaultdict(int)
Db = defaultdict(int)

for a in A:
  Da[a] += 1

for b in B:
  Db[b] += 1

Xa = [None] * N
Xb = [None] * N
ia = 0
ib = N - 1

for v, na in Da.items():
  nb = Db[v]
  #print(v, na, nb)
  if na + nb > N:
    print('No')
    exit()

  ma = ia
  mb = N - 1 - ib
  mc = ib - ia + 1

  Da[v] = 0
  Db[v] = 0

  if na + nb < mc:
    for i in range(na):
      Xa[ia] = v
      ia += 1
    for i in range(nb):
      Xb[ib] = v
      ib -= 1

  else:
    for ka in range(mc + 1):
      kb = mc - ka
      if ka <= na and na - ka <= mb and kb <= nb and nb - kb <= ma:
        break

    for i in range(ka):
      Xa[ia] = v
      ia += 1
    for i in range(kb):
      Xb[ib] = v
      ib -= 1

    for i in range(na - ka):
      Xa[-1 - i] = v
    for i in range(nb - kb):
      Xb[i] = v

    break

#print(Xa)
#print(Xb)

for v, na in Da.items():
  for i in range(na):
    Xa[ia] = v
    ia += 1
for v, nb in Db.items():
  for i in range(nb):
    Xb[ib] = v
    ib -= 1

print('Yes')

X = sorted([(a, b) for a, b in zip(Xa, Xb)])
print(' '.join([str(b) for _, b in X]))
