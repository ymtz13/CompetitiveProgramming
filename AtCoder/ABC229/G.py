S = input()
K = int(input())

nY = S.count('Y')

A = []
streak = None
for c in S:
  if c == 'Y':
    if streak is None:
      streak = 0
    else:
      A.append(streak)
      streak = 0

  elif streak is not None:
    streak += 1

A += [1 << 40] * (len(S) + 10)

B = [0]
for a in A:
  B.append(B[-1] + a)

if nY <= 1:
  print(nY)
  exit()


def check(X):
  v = 0
  for i in range(X - 1):
    v += min(i + 1, X - 1 - i) * A[i]

  retval = v
  l = X // 2
  for i in range(nY):
    v += B[X + i] - B[X + i - l]
    v -= B[i + l] - B[i]
    retval = min(retval, v)

  return retval <= K


ok = 1
ng = nY + 1

while ng - ok > 1:
  tgt = (ok + ng) // 2

  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)