from collections import defaultdict


def ans(ans):
  print(ans)
  exit()


N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)

for a in A:
  D[a] += 1

if len(D) > 2: ans('No')

if len(D) == 1:
  a = list(D.keys())[0]
  ans('Yes' if a <= N // 2 or a == N - 1 else 'No')

if len(D) == 2:
  (a1, n1), (a2, n2) = sorted(list(D.items()))

  if a2 - a1 != 1: ans('No')
  if n2 == 1: ans('No')
  if a2 > n1 and a2 <= n1 + n2 // 2: ans('Yes')
  ans('No')
