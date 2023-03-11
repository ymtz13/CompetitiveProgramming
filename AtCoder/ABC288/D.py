N, K = map(int, input().split())
A = list(map(int, input().split()))

Af = A[:]
Pf = []
for i in range(N - K + 1):
  v = Af[i]
  Pf.append(tuple(Af[i:i + K]))
  for j in range(i, i + K):
    Af[j] -= v


def solve(A, K):
  A = A[:]
  N = len(A)
  for i in range(N - K + 1):
    v = A[i]
    for j in range(i, i + K):
      A[j] -= v

  return A.count(0) == N


Q = int(input())
ans = []

Z10 = [0] * 10

for _ in range(Q):
  l, r = map(int, input().split())
  l -= 1
  r -= 1

  n = r - l + 1

  if n <= 8:
    ans.append(solve(A[l:r + 1], K))

  else:
    pl = Pf[l]
    pr = Pf[r - K + 1]
    d = [A[l + i] - pl[i] for i in range(K)]
    ans.append(solve(d + [0] * (n % K) + list(pr), K))

for a in ans:
  print('Yes' if a else 'No')
