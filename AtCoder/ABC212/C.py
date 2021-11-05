N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))


def f(A, B):
  B = [None] + B[:]
  ans = 10**20

  ib = 0
  for a in A:
    while ib + 1 < len(B) and B[ib + 1] <= a:
      ib += 1
    #print('pair', a, B[ib])
    if ib > 0: ans = min(ans, a - B[ib])

  return ans


print(min(f(A, B), f(B, A)))
