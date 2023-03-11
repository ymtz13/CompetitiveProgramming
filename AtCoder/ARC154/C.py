def dedupe(A):
  prev = None
  dA = []
  for a in A:
    if a != prev:
      dA.append(a)
      prev = a

  if len(dA) > 1 and dA[0] == dA[-1]: dA = dA[:-1]

  return dA


T = int(input())

ans = []
for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  if A == B:
    ans.append('Yes')
    continue

  if N == 1:
    ans.append('No')
    continue

  J = None
  for i in range(N):
    j = (i + 1) % N
    if B[i] == B[j]:
      J = j
      break

  if J is None:
    ans.append('No')
    continue

  dA = dedupe(A)
  dB = dedupe(B)

  if len(dA) < len(dB):
    ans.append('No')
    continue

  dB2 = dB + dB
  M = len(dB)
  ok = False

  for s in range(M):
    dBB = dB2[s:s + M]
    c = 0
    for a in dA:
      if c < M and a == dBB[c]: c += 1

    if c == M:
      ok = True
      break

  ans.append('Yes' if ok else 'No')

for a in ans:
  print(a)
