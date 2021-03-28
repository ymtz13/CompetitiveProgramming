N = int(input())
S = list(map(int, input()))[::-1]
X = input()[::-1]

D = {0}
for s, x in zip(S, X):
  D_ = set()
  if x=='A':
    for z in range(7):
      if z*10%7 in D and (z*10+ s)%7 in D: D_.add(z)
  else:
    for z in range(7):
      if z*10%7 in D or (z*10+ s)%7 in D: D_.add(z)
  D = D_

print('Takahashi' if 0 in D else 'Aoki')
