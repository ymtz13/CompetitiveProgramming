oa = ord('a')

N, K = map(int, input().split())
S = input()

for p in range(1, N + 1):
  if N % p != 0: continue
  q = N // p

  C = [[0] * 26 for _ in range(p)]
  for i, c in enumerate(S):
    C[i % p][ord(c) - oa] += 1

  k = 0
  for cnt in C:
    k += q - max(cnt)

  if k <= K:
    print(p)
    exit()
