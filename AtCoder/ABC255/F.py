from sys import setrecursionlimit

setrecursionlimit(1 << 20)

N = int(input())
P = list(map(int, input().split()))
I = list(map(int, input().split()))

if P[0] != 1:
  print(-1)
  exit()

L = [None] * (N + 1)
for l, i in enumerate(I):
  L[i] = l

LC = [0] * (N + 1)
RC = [0] * (N + 1)


def solve(pl, pr, il, ir):
  if il == ir: return 0
  root = P[pl]

  # print(P[pl:pr], I[il:ir])
  if pr - pl != ir - il:
    print(-1)
    exit()

  if pr - pl == 1:
    if P[pl] != I[il]:
      print(-1)
      exit()

    return root

  iroot = L[root]
  nl = iroot - il
  nr = ir - iroot - 1
  LC[root] = solve(pl + 1, pl + 1 + nl, il, iroot)
  RC[root] = solve(pl + 1 + nl, pr, iroot + 1, ir)
  return root


solve(0, N, 0, N)

for lc, rc in zip(LC[1:], RC[1:]):
  print(lc, rc)
