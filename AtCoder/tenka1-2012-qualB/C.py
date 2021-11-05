N = int(input())
M = 24 * 60
T = []
for _ in range(N):
  s, e = input().split()
  sh, sm = map(int, s.split(':'))
  eh, em = map(int, e.split(':'))

  s = sh * 60 + sm
  e = eh * 60 + em

  if e <= M:
    T.append(((s, e), ))

  else:
    T.append(((s, M), (0, e - M)))

E = [[0] * N for _ in range(N)]
for i, ti in enumerate(T):
  for j, tj in enumerate(T[i + 1:], i + 1):
    ovlp = 0
    for si, ei in ti:
      for sj, ej in tj:
        if ei <= sj or ej <= si: continue
        ovlp = 1

    E[i][j] = E[j][i] = ovlp

for e in E:
  print(e)

memo = [None] * (1 << 20)
memo[0] = [None] * N


def dfs(b):
  if memo[b] is not None: return memo[b]

  retval = 20
  for i in range(N):
    k = 1 << i
    if b & k == 0: continue

    r = b - k

  memo[b] = retval
  return retval


ans = dfs((1 << N) - 1)
print(ans)
