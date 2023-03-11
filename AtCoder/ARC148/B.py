N = int(input())
S = input()

if S.count('p') == 0:
  print(S)
  exit()

for L, c in enumerate(S):
  if c == 'p': break

K = 'z' * N
for R in range(L, N):
  if S[R] == 'd': continue
  if R < N - 1 and S[R + 1] == 'p': continue

  X = ''.join('p' if c == 'd' else 'd' for c in reversed(S[L:R + 1]))
  X += S[R + 1:]

  if X < K: K = X

print(S[:L] + K)
