def f(V, a):
  for i, v in enumerate(V):
    b = 1 << i
    if not a & b: continue
    if v is None: return (i, a)
    a ^= v

  return (-1, -1)


T = int(input())

Ans = []
for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  S = input()

  V = [None] * 60
  ans = 0
  for s, a in zip(S[::-1], A[::-1]):
    i, x = f(V, a)

    if s == '0':
      if i != -1: V[i] = x
    else:
      if i != -1:
        ans = 1
        break

  Ans.append(ans)

for ans in Ans:
  print(ans)
