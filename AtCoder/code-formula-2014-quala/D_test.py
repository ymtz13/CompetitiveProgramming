from itertools import permutations

N, M = map(int, input().split())


def count(P):
  typed = [False] * M
  n = 0
  cnt = 0
  for p in P:
    if p == n:
      cnt += 1
      n += 1
      while n < N and typed[n]:
        cnt += 1
        n += 1
      if n == N: break

    else:
      typed[p] = True
      cnt += 2
  
  return cnt


all = 0
s = 0
for P in permutations(list(range(M))):
  all += 1
  s += count(P)

print(s / all)
