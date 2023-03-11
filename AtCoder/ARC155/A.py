T = int(input())

Ans = []
for _ in range(T):
  N, K = map(int, input().split())
  S = input()

  Q = K // (2 * N)
  if Q % 2 == 1:
    S = S[::-1]

  K = K % (2 * N)

  ans = 'Yes'

  X = [None] * K
  for i, c in enumerate(S[:K], 1):
    X[-i] = c

  for i, c in enumerate(S[::-1][:K]):
    if X[i] is not None and X[i] != c:
      ans = 'No'
    X[i] = c

  X = ''.join(X)
  XS = X + S
  SX = S + X

  if XS != XS[::-1]: ans = 'No'
  if SX != SX[::-1]: ans = 'No'

  Ans.append(ans)

for ans in Ans:
  print(ans)
