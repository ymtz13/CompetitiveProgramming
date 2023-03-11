def f(S):
  p = None
  ret = []
  s = 0
  for c in S:
    if c != p and p is not None:
      ret.append((p, s))
      s = 0

    p = c
    s += 1

  ret.append((p, s))
  return ret


S = input()
T = input()

SX = f(S)
TX = f(T)

if len(SX) != len(TX):
  print('No')
  exit()

ans = 'Yes'
for (cs, ns), (ct, nt) in zip(SX, TX):
  if cs != ct or ns > nt or (ns == 1 and nt > 1): ans = 'No'

print(ans)
