N = int(input())
S = [input() for _ in range(N)]

E = [[] for _ in range(N)]
for i, si in enumerate(S):
  for j, sj in enumerate(S):
    if i == j: continue
    if si[-1] == sj[0]:
      E[i].append(j)

P = 1 << N

S = [None] * N * P

for n in range(N):
  S[n] = False

for p in range(P - 1):
  for n in range(N):
    if p & (1 << n): continue

    win = False

    for e in E[n]:
      b = 1 << e
      if not (p & b): continue
      pp = p - b

      if S[pp * N + e] == False:
        win = True

    S[p * N + n] = win

win = False
for n in range(N):
  b = 1 << n
  p = P - 1 - b

  if S[p * N + n] == False:
    win = True

print('First' if win else 'Second')
