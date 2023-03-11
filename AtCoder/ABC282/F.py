N = int(input())

M = [[None] * 4001 for _ in range(4001)]

#for k in range(12):
P = []

ff = 1
for k in range(12):
  K = 1 << k
  D = []
  for C in range(K, N + 1, K * 2):
    # left
    for L in range(C, C - K, -1):
      vl = min(L, N)
      vr = min(C, N)
      D.append((vl, vr))
      M[vl][vr] = ff
      ff += 1

    # right
    for R in range(C + 1, C + 1 + K):
      vl = min(C + 1, N)
      vr = min(R, N)
      D.append((vl, vr))
      M[vl][vr] = ff
      ff += 1

  print(D)

  P.extend(D)

print(len(P))
for vl, vr in P:
  print(vl, vr)

Q = int(input())
for _ in range(Q):
  L, R = map(int, input().split())

  X = R - L + 1

  for k in range(14, -1, -1):
    K = 1 << k
    if X >= K: break

  ng = -1
  ok = N + 10
  while ok - ng > 1:
    tgt = (ok + ng) // 2

    if (2 * tgt + 1) * K >= L:
      ok = tgt
    else:
      ng = tgt

  C = (2 * tgt + 1) * K

  print(K, L, C, C + 1, R)
  a = M[L][C] if L <= C else None
  b = M[C + 1][R] if C + 1 <= R else None

  if a is None: a = b
  if b is None: b = a
  print(a, b)
