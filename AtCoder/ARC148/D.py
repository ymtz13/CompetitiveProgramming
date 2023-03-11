from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

C = defaultdict(int)
for a in A:
  C[a] += 1

isBobWinner = True

if M % 2 == 1:
  for c in C.values():
    if c % 2 == 1: isBobWinner = False

else:
  H = M // 2

  checked = set()
  npair = 0
  for k1, c1 in C.copy().items():
    if k1 in checked: continue

    k2 = (k1 + H) % M
    c2 = C[k2]

    if c1 % 2 != c2 % 2:
      isBobWinner = False

    npair += min(c1, c2)

    checked.add(k1)
    checked.add(k2)

  if npair % 2 == 1: isBobWinner = False

print('Bob' if isBobWinner else 'Alice')
