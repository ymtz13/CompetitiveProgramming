mod = 998244353

N = int(input())
C = [tuple(map(int, input().split())) for _ in range(N)]

dpA = dpB = 1

for i, (a, b) in enumerate(C[1:], 1):
  aprev, bprev = C[i - 1]

  dpAnext = dpBnext = 0

  if aprev != a: dpAnext += dpA
  if bprev != a: dpAnext += dpB
  if aprev != b: dpBnext += dpA
  if bprev != b: dpBnext += dpB

  dpA = dpAnext % mod
  dpB = dpBnext % mod

ans = (dpA + dpB) % mod
print(ans)
