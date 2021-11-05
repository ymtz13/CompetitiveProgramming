nR, nG, nB = map(int, input().split())


def count(L, N):
  L = max(L, -(N - 1) // 2)
  R = L + N - 1
  aL = abs(L)
  aR = abs(R)

  if L > 0:
    n = aR * (aR + 1) // 2 - (aL - 1) * aL // 2
  else:
    n = aR * (aR + 1) // 2 + (aL + 1) * aL // 2

  return n


ans = 1 << 60
for L in range(-300, 301):
  R = L + nG - 1
  aL = abs(L)
  aR = abs(R)

  if R < 0:
    mG = aL * (aL + 1) // 2 - (aR - 1) * aR // 2
  elif L > 0:
    mG = aR * (aR + 1) // 2 - (aL - 1) * aL // 2
  else:
    mG = aR * (aR + 1) // 2 + (aL + 1) * aL // 2

  mR = count(-100 - (L - 1), nR)
  mB = count(-100 + (R + 1), nB)

  ans = min(ans, mG + mR + mB)

print(ans)
