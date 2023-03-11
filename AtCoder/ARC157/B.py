def solve(N, K, S):
  if S.count('X') == N:
    return max(0, K - 1)

  ans = 0

  prev = None
  X = []
  x = 0
  for c in S:
    if c == 'Y':
      if prev == 'Y':
        ans += 1
      X.append(x)
      x = 0
    else:
      x += 1
    prev = c

  X.append(x)

  X = sorted(X[1:-1])
  for x in X:
    if x == 0: continue

    v = min(K, x)
    ans += v
    if v == x: ans += 1

    K -= v
    if K == 0: break

  return ans + K


N, K = map(int, input().split())
S = input()

cX = S.count('X')

if K > cX:
  KK = N - K
  SS = ''.join(['X' if c == 'Y' else 'Y' for c in S])

  ans = solve(N, KK, SS)

else:
  ans = solve(N, K, S)

print(ans)
