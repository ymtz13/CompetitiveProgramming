N, K = map(int, input().split())

if N == 1:
  print('Yes')
  print(0, 1)
  exit()

if K == N or K % 2 == 0:
  print('No')
  exit()

print('Yes')


def basis(N, K):
  X = [(1 << (K + 1)) - 1 - (1 << n) for n in range(K + 1)]

  for n in range(K + 1, N):
    X.append((1 << (n + 1)) - (1 << (n + 1 - K)))

  return X


def solve(N, K):
  B = basis(N, K)

  A = [0, B[0]]
  for i in range(2, 1 << N):
    for l in range(N, 0, -1):
      if i & (1 << l): break

    j = (1 << (l + 1)) - 1 - i
    A.append(B[l] ^ A[j])

  print(' '.join(map(str, A)))


solve(N, K)
